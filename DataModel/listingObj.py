from DataModel.fs_package_model import ListingDataRow

class ListingObj():
    def __init__(self, listingID = -1, listingName = '', priceProd = 0, soldCount = 0, seenCount = 0,  reviewScore = 0, reviewCount = 0, storeArea = '', storeName = '', listingURL = '', listingImgURL = '', timestamp = 0, listingStock = 0):
        self.listingName    = listingName
        self.listingID      = listingID
        self.listingURL     = listingURL
        self.listingImgURL  = listingImgURL
        self.storeName      = storeName
        self.storeArea      = storeArea

        self.dataRow        = None
        # self.dataRow = ListingDataRow(soldCount,seenCount,listingStock,reviewCount,reviewScore,priceProd)

    def setDataRow(self, soldCount, seenCount, listingStock, reviewCount, reviewScore, priceProd):
        self.dataRow = ListingDataRow(soldCount,seenCount,listingStock,reviewCount,reviewScore,priceProd)