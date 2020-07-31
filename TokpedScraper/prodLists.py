import time

class listingObj():
    def __init__(self, nameProd = '', priceProd = 0, soldCount = 0, seenProd = 0,  reviewScore = 0, reviewCount = 0, storeArea = '', storeName = '', listingUrl = '', timestamp = 0):
        self.nameProd = nameProd
        self.priceProd = priceProd
        self.storeArea = storeArea
        self.listingUrl = listingUrl

        self.soldCount = soldCount
        self.seenProduct = seenProd
        self.reviewScore = reviewScore
        self.reviewCount = reviewCount
        self.storeName = storeName

        self.timestamp = timestamp #Stored as (int) seconds after Epoch (in UTC)

    def toString(self):
        print("-------------------")
        print("Name: {}".format(self.nameProd))
        print("Price: {}".format(self.priceProd))
        # print("Url: {}".format(self.listingUrl))
        print("SoldCount: {}".format(self.soldCount))
        print("Seen: {}".format(self.seenProduct))
        print("ReviewScore: {}".format(self.reviewScore))
        print("ReviewCount: {}".format(self.reviewCount))
        print("StoreName: {}".format(self.storeName))
        print("StoreArea: {}".format(self.storeArea))
        print("Timestamp: {}".format(time.ctime(self.timestamp)))  

    def getData(self):
        x = [self.timestamp, self.nameProd, self.priceProd, self.soldCount, self.seenProduct, self.reviewScore, self.reviewCount, self.storeName, self.storeArea, self.listingUrl]

        # ["Timestamp","Listing Name","Listing Price","Sold","Seen","Review Score","Review Count","Store Name","Store Area","URL"]

        return x
# class ProdList():
#     def __init__(self, listOfProds):
#         self.listP = listOfProds