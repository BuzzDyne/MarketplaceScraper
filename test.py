from FsPackage.fs_module import FsModule
import FsPackage.utils as u
from DataModel.fs_package_model import ListingDataRow

from ScraperPackage.scraper_module import Scraper

from app import App

################## Start of IntegrationTest ##################

app = App()
app.createNewListingData()
# app.updateListingData()



################## End of IntegrationTest ##################
################## Start of ScraperModule ##################

# sc = Scraper()

# print(sc.getShopNameByDomain("tokorrj"))

# x = sc.scrapeInitialListing("https://www.tokopedia.com/nanokomputer/processor-amd-ryzen-3-3100-matisse-am4-4-core-gen-zen-2-cpu")
# x = sc.scrapeListingDataRow(869760736)
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