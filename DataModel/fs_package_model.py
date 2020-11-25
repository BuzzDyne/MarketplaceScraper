from datetime import datetime
from ScraperPackage.scraper_status_code import ScraperStatusCode as STATUS
import pytz

class ListingDataRow():
    """A Model class used to contain a single Listing Data row to be pushed to DB"""

    def __init__(self, sold=None, seen=None, stock=None, reviewCount=None, reviewScore=None, price=None, ts=None, statusCode=None):
        self.ts             = datetime.now(tz=pytz.timezone('Asia/Jakarta'))
        self.sold           = sold          if sold is not None else -1
        self.seen           = seen          if seen is not None else -1
        self.stock          = stock         if stock is not None else -1
        self.reviewCount    = reviewCount   if reviewCount is not None else -1
        self.reviewScore    = reviewScore   if reviewScore is not None else -1   # 0-100
        self.price          = price         if price is not None else -1
        # 200 [Success], 404 [Not Found], 0 [Unknown Error]
        self.statusCode     = statusCode    if statusCode is not None else STATUS.UNKNOWN_ERROR

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

class ExistingListingObj():

    def __init__(self, listingID, docAddr):
        self.listingID  = listingID
        self.docAddr    = docAddr

    def toDict(self):
        return {
            u'url'      : self.url,
            u'docAddr'  : self.docAddr
        }

class NewListingUrl():

    def __init__(self, url, selfDocAddr, users):
        self.url            = url
        self.selfDocAddr    = selfDocAddr
        self.users          = users

    def toDict(self):
        return {
            u'url'      : self.url,
            u'docAddr'  : self.docAddr,
            u'users'    : self.users
        }

