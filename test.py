from FsPackage.fs_module import FsModule
import FsPackage.utils as u
from DataModel.fs_package_model import ListingDataRow

from ScraperPackage.scraper_module import Scraper

from ClientSimulatorPackage.client_simulator import ClientSimulator
import ClientSimulatorPackage.utils as CspUtils

from app import App

################## Start of IntegrationTest ##################

app = App()
# app.createNewListingData()
app.updateListingData()



################## End of IntegrationTest ##################
################## Start of ScraperModule ##################

# sc = Scraper()

# print(sc.getShopNameByDomain("tokorrj"))

# x = sc.scrapeInitialListing("https://www.tokopedia.com/nanokomputer/processor-amd-ryzen-3-3100-matisse-am4-4-core-gen-zen-2-cpu")
# x = sc.scrapeListingDataRow(613013164)
# print(x.toDict())




################### End of ScraperModule #################
#################### Start of FsModule ###################

# fs = FsModule()

# x = fs.getExistingListingURLs()
# x = fs.getNewListingURLs()

# fs.createListing("RTX 2080","123","Enter Komputer","Jakarta Barat")

# data = ListingDataRow(55,55,45,555,555544)
# fs.insertSingleListingDataRow("123", data)

# print(fs.getNewListingURLs()[0].toDict())


# Tagify Example
# pName = "RAZER BLADE PRO 4K 32GB i7 GTX 1080 LAPTOP GAMING NO MACBOOK ALIENWARE"
# te = "1 2 3 4 5 6 7 8"
# e = "Laptop Gaming RAZER BLADE 15 - i7 8750 16GB 512GB GTX1070 8GB W10 15.6 - Hitam"


# res = u.tagifyListingName(e)
# # print(res)
# print(len(res))

# res = u.tagifyListingNameV2(e)
# # print(res)
# print(len(res))


################## End of FsModule ##################
################## Start of ClientSimulator ##################

# client = ClientSimulator("admin")
# # client.createNewUser("First User", "")

# # UrlList Example
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

# client.createNewListingURLs(urlList)

################## End of ClientSimulator ##################