from datetime import datetime
import pytz

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import FsPackage.utils as utils

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
        #     u'currPrice'    : '',
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
        u'currPrice'    : 0,
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

      parentRef.add(payload)

    def readDocument(self, target):
      doc = self.db.document(target).get() 
      return doc.to_dict()