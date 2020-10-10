from datetime import datetime
import pytz

class ListingDataRow():
    """A Model class used to contain a single Listing Data row to be pushed to DB"""

    def __init__(self, sold, stock, reviewCount, reviewScore, price, ts=None):
        self.ts             = datetime.now(tz=pytz.timezone('Asia/Jakarta'))
        self.sold           = sold
        self.stock          = stock
        self.reviewCount    = reviewCount
        self.reviewScore    = reviewScore
        self.price          = price

        if(ts is not None):
            self.ts = ts

    def toDict(self):
        return {
            u'ts'           : self.ts,
            u'sold'         : self.sold,
            u'stock'        : self.stock,
            u'reviewCount'  : self.reviewCount,
            u'reviewScore'  : self.reviewScore,
            u'price'        : self.price
        }