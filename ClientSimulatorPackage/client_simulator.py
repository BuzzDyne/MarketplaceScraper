import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# from ClientSimulatorPackage.utils import utils
import utils

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
        payload['url'] = url
        ref = parentRef.add(payload)

        print('Successfully Added Doc {} out of {} ({})'.format(i, totalCount, ref[1].path))
        i = i+1

client = ClientSimulator("admin")
# client.createNewUser("First User", "")

# UrlList Example
  # urlList = [
  #   'https://www.tokopedia.com/destinycomputer/venom-rx-nemesis-case?src=topads',
  #   'https://www.tokopedia.com/techinstore/casing-pc-cooler-master-masterbox-q300l?src=topads',
  #   'https://www.tokopedia.com/nobel-computer/corsair-crystal-280x-rgb-tempered-glass-gaming-case-white?src=topads',
  #   'https://www.tokopedia.com/hellomoindonesia/carbon-case-casing-black-iphone-5-5s-se-6-6s-6-6s-7-7-8-8-x-iphone-se?whid=0',
  #   'https://www.tokopedia.com/futarishop/custom-case-bebas-suka-suka-cetak-foto-casing-custom-hp?whid=0',
  #   'https://www.tokopedia.com/toko-ws/casing-hardisk-external-hdd-external-case-2-5-usb-3-0-orico-2139u3?whid=0',
  #   'https://www.tokopedia.com/lbagstore/dual-sim-card-adapter-hybrid-sim-card-extender-microsd-card-converter-nano?whid=0',
  #   'https://www.tokopedia.com/rendevousind/casing-custom-case-fullprint-hardcase-samsung-iphone-xiaomi-sony-dll?whid=0',
  #   'https://www.tokopedia.com/kortingstore/case-iphone-77-plus-66s-slim-silicone-casing-black-premium?whid=0',
  #   'https://www.tokopedia.com/spigen-official/iphone-xs-max-xs-x-xr-case-spigen-pattern-softcase-liquid-air-xs-max?whid=0',
  #   'https://www.tokopedia.com/spigen-official/spigen-ultra-hybrid-2-case-for-iphone-7-plus-iphone-8-plus-black-d679?whid=0',
  #   'https://www.tokopedia.com/supermassive-ina/promo-orico-2139u3-casing-hardisk-transparan-25-usb-30-enclosure?whid=0',
  #   'https://www.tokopedia.com/spigen-official/case-samsung-galaxy-a51-a71-spigen-liquid-air-softcase-black-casing-a71?whid=0',
  #   'https://www.tokopedia.com/toko-ws/casing-hardisk-external-hdd-external-case-2-5-usb-3-0-vivan-vshd1?whid=0',
  #   'https://www.tokopedia.com/spigen-official/case-iphone-11-pro-max-11-pro-11-spigen-liquid-crystal-casing-space-crystal-11-pro?whid=0',
  #   'https://www.tokopedia.com/asenaru/asenaru-iphone-11-11-pro-11-pro-max-casing-super-slim-signature-case-hitam-iphone-11?whid=0',
  #   'https://www.tokopedia.com/goru/case-original-silicon-apple-iphone-6-6s-7-8-plus-hard-soft-casing?whid=0',
  #   'https://www.tokopedia.com/pinegadgetacc/case-iphone-x-xs-xr-xs-max-fuze-anti-crack-baby-skin-casing-hitam-xr?whid=0',
  #   'https://www.tokopedia.com/breakboxstore/softcase-leather-iphone-6-6-7-7-8-8-plus-x-casing-jelly-case-kulit-hitam?whid=0',
  #   'https://www.tokopedia.com/megacasing/baby-skin-case-iphone-5-5s-5se-6-6s-6-6-plus-7-7-plus-hardcase-casing?whid=0',
  #   'https://www.tokopedia.com/breakboxstore/anti-crack-iphone-5-5s-se-6-6s-plus-7-7-plus-8-8-plus-case-fuze-casing?whid=0'
  # ]

client.createNewListingURLs(urlList)