class prodObj():
    def __init__(self, nameProd = '', priceProd = '', soldCount = '', seenProd = '',  reviewScore = '', reviewCount = '', storeArea = '', storeName = '', listingUrl = ''):
        self.nameProd = nameProd
        self.priceProd = priceProd
        self.storeArea = storeArea
        self.listingUrl = listingUrl

        self.soldCount = soldCount
        self.seenProduct = seenProd
        self.reviewScore = reviewScore
        self.reviewCount = reviewCount
        self.storeName = storeName

    def toString(self):
        print("-------------------")
        print("Name: {}".format(self.nameProd))
        print("Price: {}".format(self.priceProd))
        print("StoreArea: {}".format(self.storeArea))
        # print("Url: {}".format(self.listingUrl))
        print("SoldCount: {}".format(self.soldCount))
        print("Seen: {}".format(self.seenProduct))
        print("ReviewScore: {}".format(self.reviewScore))
        print("ReviewCount: {}".format(self.reviewCount))
        print("StoreName: {}".format(self.storeName))
        

# class ProdList():
#     def __init__(self, listOfProds):
#         self.listP = listOfProds