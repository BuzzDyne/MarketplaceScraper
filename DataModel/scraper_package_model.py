class ListingObj():
    def __init__(self, listingID = -1, listingName = '', priceProd = 0, soldCount = 0, seenCount = 0,  reviewScore = 0, reviewCount = 0, storeArea = '', storeName = '', listingUrl = '', timestamp = 0, listingStock = 0):
        self.listingID = listingID
        self.listingName = listingName
        self.priceProd = priceProd
        self.storeArea = storeArea
        self.listingUrl = listingUrl

        # 0 = No Stock, 9999 = Available
        self.listingStock = listingStock

        self.soldCount = soldCount
        self.seenCount = seenCount
        self.reviewScore = reviewScore #(int, 0-50)
        self.reviewCount = reviewCount
        self.storeName = storeName

        self.timestamp = timestamp #Stored as (int) seconds after Epoch (in UTC)