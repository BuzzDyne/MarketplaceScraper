from FsPackage.fs_module import FsModule
import FsPackage.utils as u
from DataModel.fs_package_model import ListingDataRow

from ScraperPackage.scraper_module import Scraper


################## Start of ScraperModule ##################

sc = Scraper()

print(sc.getShopNameByDomain("tokorrj"))











################### End of ScraperModule #################
#################### Start of FsModule ###################

# fs = FsModule()

# fs.createListing("RTX 2080","123","Enter Komputer","Jakarta Barat")

# data = ListingDataRow(55,55,45,555,555544)
# fs.insertSingleListingDataRow("123", data)

# print(fs.getNewListingURLs()[0].toDict())


# Tagify Example
# res = u.tagifyListingName("RAZER BLADE PRO 4K 32GB i7 GTX 1080 LAPTOP GAMING NO MACBOOK ALIENWARE")
# print(res)
# print(len(res))

################## End of FsModule ##################