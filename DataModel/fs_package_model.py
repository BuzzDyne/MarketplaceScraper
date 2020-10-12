from datetime import datetime
import pytz

class ListingDataRow():
    """A Model class used to contain a single Listing Data row to be pushed to DB"""

    def __init__(self, sold, seen, stock, reviewCount, reviewScore, price, ts=None):
        self.ts             = datetime.now(tz=pytz.timezone('Asia/Jakarta'))
        self.sold           = sold
        self.seen           = seen
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
            u'seen'         : self.seen,
            u'stock'        : self.stock,
            u'reviewCount'  : self.reviewCount,
            u'reviewScore'  : self.reviewScore,
            u'price'        : self.price
        }

class ExistingListingUrl():

    def __init__(self, url, docAddr):
        self.url        = url
        self.docAddr    = docAddr

    def toDict(self):
        return {
            u'url'      : self.url,
            u'docAddr'  : self.docAddr
        }

class NewListingUrl():

    def __init__(self, url, docAddr, users):
        self.url        = url
        self.docAddr    = docAddr
        self.users      = users

    def toDict(self):
        return {
            u'url'      : self.url,
            u'docAddr'  : self.docAddr,
            u'users'    : self.users
        }

