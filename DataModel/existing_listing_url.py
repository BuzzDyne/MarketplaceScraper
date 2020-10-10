class ExistingListingUrl():

    def __init__(self, url, docAddr):
        self.url        = url
        self.docAddr    = docAddr

    def toDict(self):
        return {
            u'url'      : self.url,
            u'docAddr'  : self.docAddr
        }