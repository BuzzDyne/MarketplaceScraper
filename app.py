class App:
    def __init__(self):
        self.fs = FsModule()
        self.sc = Scraper()

    def createNewListingData(self):
      """
      1. Get 'NewListings' from db
      2. Scrape data
      3. Create a new Listing Doc
      4. TODO Delete/Mark created 'NewListing'
      """
        newListingUrls = self.fs.getNewListingURLs()

        for obj in newListingUrls:
            l = self.sc.scrapeInitialListing(obj.url)

            self.fs.createListing(l.listingName, l.listingID, l.listingURL, l.storeName, l.storeArea)
            self.fs.insertSingleListingDataRow(l.listingID, l.dataRow)

    def updateListingData(self):
      """
        1. Get all Listing Document from db
        2. Scrape data
        3. create a new DataRow Doc inside each Listing Doc"""
        listObj = self.fs.getExistingListingURLs()

        for obj in listObj:
            dataRow = self.sc.scrapeListingDataRow(obj.listingID)
            self.fs.insertSingleListingDataRow(obj.listingID, dataRow)