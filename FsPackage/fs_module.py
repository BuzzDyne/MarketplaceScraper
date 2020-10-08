from datetime import datetime
import pytz

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import FsPackage.utils as utils
from DataModel.listing_data_row import ListingDataRow

cred = credentials.Certificate("pricetrend-8d62c-ecd1490085a6.json")

addr = {
  "NewListing"      : "Scraper/newListing",
  "ExistingListing" : "Scraper/existingListing",
  "Listings"        : "Listings"
}

class FsModule:
    """Handles CRUD operation to the Firestore DB
    
    Requires Firestore's JSON Auth Key to be placed on the same dir as this module"""

    def __init__(self):
      firebase_admin.initialize_app(cred)        
      self.db = firestore.client()

    ################ Scraper ################
    def getNewListingURLs(self):
      """Returns a list of new listing urls"""
      doc = self.db.document(addr['NewListing']).get()
      return doc.to_dict()["urls"]

    ################ Listings ################
    def createListing(self, listingName, listingID, storeName, storeArea):
      """Write a new Listing Document given the initial data"""
      # Data sample 
        # {
        #   u'tags'         : [],
        #   u'stats'        : {
        #     u'activeTracking' : 0,
        #     u'bought'         : 0
        #   },
        #   u'listingName'  : '',
        #   u'listingID'    : '',
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
        u'stock'        : 0,
        u'reviewCount'  : 0,
        u'reviewScore'  : 0,
        u'price'        : 0,
        u'prevPrice'    : 0
      }

      payload = {
        u'tags'         : utils.tagifyListingName(listingName),
        u'stats'        : {
          u'activeTracking' : 0,
          u'bought'         : 0
        },
        u'listingName'  : listingName,
        u'listingID'    : listingID,
        u'storeName'    : storeName,
        u'storeArea'    : storeArea,
        u'latestData'   : latestData
      }

      ref = parentRef.add(payload)

      # print(ref[1].path)

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


    def readDocument(self, target):
      doc = self.db.document(target).get() 
      return doc.to_dict()