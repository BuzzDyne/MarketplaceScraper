from firebase_admin import messaging
import firebase_admin
import requests
import json

from FsPackage.scraper_enum import ScraperStatusCode as Code

fsCredPath = "pricetrend-8d62c-ecd1490085a6.json"

class FcmModule:
    requestNotifTitle = {
        Code.NOT_FOUND  : "Requested Listing was not found",
        Code.EXISTED    : "Requested Listing existed",
        Code.CREATED    : "Requested Listing created"
    }

    def __init__(self):
        cred = firebase_admin.credentials.Certificate(fsCredPath)
        # self.app = firebase_admin.initialize_app(cred)

    def sendNotif(self, token, title, body):
        notif = messaging.Notification(
            title=title,
            body=body
        )

        msg = messaging.Message(
            notification=notif,
            token=token
        )

        response = messaging.send(
            message=msg
        )

        print("Notif sent with response:", response)

    def sendListingRequestResultNotif(self, token, statusCode, listingUrl):
        self.sendNotif(token, self.requestNotifTitle[statusCode], listingUrl)

    def sendNotifHttp(self, deviceToken):
        serverToken = "AAAA89y-mik:APA91bFniaiP_B4JakSoYypMzHLQH_dbsRa2S39O9qQ_9BD9ZBJ5V1NzVfJ7mZO6UDgFRl3eGK6YtbkLkBnV3mdIHY3y9QYFM9yzHN4hBKuAFNEHFXSyrNUDuvW4RecpRJN6S4oHKlig"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

        body = {
                'notification': {
                    'title': 'Sending push form python script',
                    'body': 'New Message'
                    },
                'to': deviceToken,
                'priority': 'high',
        }
        
        response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
        print(response.status_code)

        print(response.json())
        