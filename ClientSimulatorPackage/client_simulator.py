import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

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


client = ClientSimulator("uid_1")
# client.createNewUser("First User", "")

