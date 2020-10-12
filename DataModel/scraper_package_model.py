from DataModel.fs_package_model import ListingDataRow

class ListingObj():
    def __init__(self, listingID = -1, listingName = '', priceProd = 0, soldCount = 0, seenCount = 0,  reviewScore = 0, reviewCount = 0, storeArea = '', storeName = '', listingUrl = '', timestamp = 0, listingStock = 0):
        self.listingName = listingName
        self.listingID = listingID
        self.listingUrl = listingUrl
        self.storeName = storeName
        self.storeArea = storeArea

        self.timestamp = timestamp #Stored as (int) seconds after Epoch (in UTC)
        self.priceProd = priceProd
        self.listingStock = listingStock
        self.soldCount = soldCount
        self.seenCount = seenCount
        self.reviewScore = reviewScore #(int, 0-50)
        self.reviewCount = reviewCount