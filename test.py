from datetime import datetime
import pytz

from FsPackage.fs_module import FsModule
import FsPackage.utils as u

from DataModel.listing_data_row import ListingDataRow

fs = FsModule()

# fs.createListing("RTX 2080","123","Enter Komputer","Jakarta Barat")

# data = ListingDataRow(44,44,44,544,2544)

# fs.insertSingleListingDataRow("123", data)

# print(fs.getNewListingURLs()[0].toDict())
print(fs.getNewListingURLs()[0].toDict())


# Tagify Example
# res = u.tagifyListingName("RAZER BLADE PRO 4K 32GB i7 GTX 1080 LAPTOP GAMING NO MACBOOK ALIENWARE")
# print(res)
# print(len(res))