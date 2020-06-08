class prodObj():
    def __init__(self, nameProd = '', priceProd = '', soldProd = '', storeArea = '', storeName = ''):
        self.nameProd = nameProd
        self.priceProd = priceProd
        self.soldProd = soldProd
        self.storeArea = storeArea
        self.storeName = storeName

class ProdList():
    def __init__(self, listOfProds):
        self.listP = listOfProds