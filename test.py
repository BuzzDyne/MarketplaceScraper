from FsPackage.fs_module import FsModule
import FsPackage.utils as u
from DataModel.fs_package_model import ListingDataRow

from ScraperPackage.scraper_module import Scraper

################## Start of IntegrationTest ##################

app = PriceTrendModule()
# app.createNewListingData()
app.updateListingData()




################## Start of ScraperModule ##################

# sc = Scraper()

# print(sc.getShopNameByDomain("tokorrj"))

# x = sc.scrapeInitialListing("https://www.tokopedia.com/nanokomputer/processor-amd-ryzen-3-3100-matisse-am4-4-core-gen-zen-2-cpu")
# x = sc.scrapeListingDataRow(869760736)
# print(x.toDict())




################### End of ScraperModule #################
#################### Start of FsModule ###################

# fs = FsModule()

# fs.getExistingListingURLs()

# fs.createListing("RTX 2080","123","Enter Komputer","Jakarta Barat")

# data = ListingDataRow(55,55,45,555,555544)
# fs.insertSingleListingDataRow("123", data)

# print(fs.getNewListingURLs()[0].toDict())


# Tagify Example
# res = u.tagifyListingName("RAZER BLADE PRO 4K 32GB i7 GTX 1080 LAPTOP GAMING NO MACBOOK ALIENWARE")
# print(res)
# print(len(res))

################## End of FsModule ##################