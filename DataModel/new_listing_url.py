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