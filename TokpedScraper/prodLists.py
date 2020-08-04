import time

class listingObj():
    def __init__(self, listingID = -1, nameProd = '', priceProd = 0, soldCount = 0, seenCount = 0,  reviewScore = 0, reviewCount = 0, storeArea = '', storeName = '', listingUrl = '', timestamp = 0, listingStock = 0):
        self.listingID = listingID
        self.nameProd = nameProd
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

    def toString(self):
        print("-------------------")
        print("Name: {}".format(self.nameProd))
        print("Price: {}".format(self.priceProd))
        # print("Url: {}".format(self.listingUrl))
        print("SoldColistingStockunt: {}".format(self.listingStock))
        print("SoldCount: {}".format(self.soldCount))
        print("Seen: {}".format(self.seenCount))
        print("ReviewScore: {}".format(self.reviewScore))
        print("ReviewCount: {}".format(self.reviewCount))
        print("StoreName: {}".format(self.storeName))
        print("StoreArea: {}".format(self.storeArea))
        print("Timestamp: {}".format(time.ctime(self.timestamp)))  

    def getData(self):
        x = [self.timestamp, self.listingID, self.nameProd, self.priceProd, self.listingStock, self.soldCount, self.seenCount, self.reviewScore, self.reviewCount, self.storeName, self.storeArea, self.listingUrl]

        # ["Timestamp","Listing Name","Listing Price", "Stock","Sold","Seen","Review Score","Review Count","Store Name","Store Area","URL"]

        return x
# class ProdList():
#     def __init__(self, listOfProds):
#         self.listP = listOfProds