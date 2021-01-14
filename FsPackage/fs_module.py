from datetime import datetime, timedelta
import pytz

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import FsPackage.utils as utils
from FsPackage.scraper_enum import ScraperStatusCode as SC

from DataModel.fs_package_model import ListingDataRow, ExistingListingObj, NewListingUrl

fsCredPath = "pricetrend-8d62c-ecd1490085a6.json"

addr = {
  "NewListing"      : "Scraper/newListing/UrlList",
  "Listings"        : "Listings"
}

class FsModule:
    """
      Handles CRUD operation to the Firestore DB
    
      Requires Firestore's JSON Auth Key to be placed on the same dir as this module"""

    def __init__(self):
      cred = credentials.Certificate(fsCredPath)
      firebase_admin.initialize_app(cred)
      self.db = firestore.client()

    # ScraperCol 

    def getNewListingURLs(self):
      """Returns a list of NewListingUrl obj that haven't been created its listing"""

      docs = self.db.collection(addr['NewListing']).where("statusCode", "==", SC.WAITING).get()
      
      result = []

      for doc in docs:
        result.append(NewListingUrl(doc.get('url'), doc.reference.path, doc.get('users')))

      return result

    def setNewListingDocAddr(self, selfAddr, listingDocAddr):
      """Set the 'docAddr' field of 'newListing' collection
      
      Marking the 'newListing' as successfully created at 'Listing' collection """
      docRef = self.db.document(selfAddr)

      data = {
        'isCreated'       : True,
        'listingDocAddr'  : listingDocAddr
      }

      docRef.update(data)

    def getExistingListingURLs(self):
      """Returns a list of ExistingListingUrl obj which was updated at least 20 hours ago"""
      
      staleDataTS = datetime.now(tz=pytz.timezone('Asia/Jakarta')) + timedelta(hours=-20)

      docs = self.db.collection(addr['Listings']).where('latestData.ts', '<=', staleDataTS).get()
      resList = []

      for doc in docs:
        resList.append(ExistingListingObj(doc.to_dict()['listingID'], doc.reference.path))

      return resList

    # ListingsCol 
    def createListing(self, listingName, listingID, listingUrl, listingImgURL, listingThumbURL, storeName, storeArea):
      """Write a new Listing Document given the initial data,
      then updates the existingListing document with new ListingDocAddr and listingURL

      Returns the DocAddr of newly created ListingDoc"""
      # Data sample 
        # {
        #   u'tags'         : [],
        #   u'stats'        : {
        #     u'activeTracking' : 0,
        #     u'bought'         : 0
        #   },
        #   u'listingName'  : '',
        #   u'listingID'    : '',
        #   u'listingURL'   : '',
        #   u'storeName'    : '',
        #   u'storeArea'    : '',
        #   u'latestData'   : {
        #     u'ts'           : '',
        #     u'sold'         : '',
        #     u'stock'        : '',
        #     u'reviewCount'  : '',
        #     u'reviewScore'  : '',
        #     u'price'        : '',
        #     u'prevPrice'    : ''
        #   }
        # }
      
      parentRef = self.db.collection(addr['Listings'])

      latestData = {
        u'ts'           : datetime.now(tz=pytz.timezone('Asia/Jakarta')),
        u'sold'         : 0,
        u'seen'         : 0,
        u'stock'        : 0,
        u'reviewCount'  : 0,
        u'reviewScore'  : 0,
        u'price'        : 0,
        u'prevPrice'    : 0
      }

      payload = {
        u'tags'         : utils.tagifyListingNameV2(listingName),
        u'stats'        : {
          u'activeTracking' : 0,
          u'bought'         : 0
        },
        u'listingName'  : listingName,
        u'listingID'    : listingID,
        u'listingURL'   : listingUrl,
        u'listingImgUrl': listingImgURL,
        u'listingThumbUrl': listingThumbURL,
        u'storeName'    : storeName,
        u'storeArea'    : storeArea,
        u'latestData'   : latestData
      }

      ref = parentRef.add(payload)

      return ref[1].path

    def insertSingleListingDataRow(self, listingID, data):
      """Write a new data doc of a ListingDoc (given its listingID) with the given data (ListingDataRow)
      
      1. Query the listing data (listingID)
      2. Add new doc in the 'data' subcollection
      3. Updates the 'latestData' field on parent ListingDoc"""

      # Data Type Handling
      if(type(data) is not ListingDataRow):
        print("The given data type is not 'ListingDataRow'")
        return None

      # 1. Query
      listingRef = self.db.collection(addr['Listings'])
      result_list = listingRef.where("listingID", "==", listingID).get()
      
      # Query Error Handling
      if(len(result_list) == 0):
        print('No Listing with id ({}) found!'.format(listingID))
        return None
      elif(len(result_list) > 1):
        print('More than one Listing with id ({}) found! ListingID supposed to be unique!'.format(listingID))
        return None

      # 2. Insert new doc
      parentDocAddr = result_list[0].reference.path
      trgtRef = self.db.collection(parentDocAddr+"/data")
      trgtRef.add(data.toDict())

      # 3. Update metadata
      prevPrice = result_list[0].to_dict()['latestData']['price']

      data_dict = data.toDict()
      data_dict['prevPrice'] = prevPrice
      latestData_dict = {
        'latestData': data_dict
      }

      parentRef = self.db.document(parentDocAddr)
      parentRef.update(latestData_dict)

    def updateListingWithImgUrls(self, listingDocAddr, imgUrl, thumbUrl):
      """Updates existing ListingDoc with ImgURLs

      This was used when ImgURLs werent being saved at ListingDoc creation.
      """
      listingRef = self.db.document(listingDocAddr)

      listingRef.set({
        u'listingImgURL'  : imgUrl,
        u'listingThumbURL': thumbUrl
      }, merge=True)

    # TOOLS
    def getAllExistingListingURLs(self):
      """Returns a list of ExistingListingUrl obj
      
      Was only used for 'Tools' to add images to all existing ListingDoc (This was from before ImgUrls were saved to db)"""

      docs = self.db.collection(addr['Listings']).get()
      resList = []

      print(f'Found {len(docs)} docs')

      for doc in docs:
        resList.append(ExistingListingObj(doc.to_dict()['listingID'], doc.reference.path))

      return resList

    def changeAllListingIDtoString(self):
      """Swap ALL LISTING's ID field from int to String
      
      Was only used for 'Tools'"""
      docs = self.getAllExistingListingURLs()

      for doc in docs:
        x = self.db.document(doc.docAddr)
        x.set({
          u'listingID'  : str(doc.listingID)
        }, merge=True)