import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import ClientSimulatorPackage.utils as utils

cred = credentials.Certificate("pricetrend-8d62c-ecd1490085a6.json")

class ClientSimulator:
    def __init__(self, uid):
        firebase_admin.initialize_app(cred)        
        self.db = firestore.client()
        self.uid = uid
    
    def createNewUser(self, displayName, profilePicUrl):
        parentRef = self.db.collection('Users')

        payload = {
            u'displayName'      : displayName,
            u'profilePicUrl'    : profilePicUrl,
            u'totalSaving'      : 0,
            u'trxCount'         : 0,
            u'activeTrackingsMetadata'  : [],
        }

        parentRef.document(self.uid).set(payload)

    def createNewListingURLs(self, listOfUrls):
      """Create a new NewListing Doc for element of listOfUrls given"""
      if(type(listOfUrls) != list):
        print("inside createNewListingURLs, wrong arg type.")

      parentRef = self.db.collection("Scraper/newListing/UrlList")

      payload = {
        u'isCreated'    : False,
        u'url'          : '',
        u'users'        : [self.uid]
      }

      totalCount = len(listOfUrls)
      i = 1
      for url in listOfUrls:
        payload['url'] = utils.cleanUrl(url)
        ref = parentRef.add(payload)

        print('Successfully Added Doc {} out of {} ({})'.format(i, totalCount, ref[1].path))
        i = i+1
