import logging
from datetime import datetime, timedelta
import pytz

from ScraperPackage.scraper_module import Scraper
from FsPackage.fs_module import FsModule

now = datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime("%Y-%m-%d_%H-%M-%S")
LOG_FORMAT = "%(levelname)s,%(asctime)s.%(msecs)03d,%(module)s<%(funcName)s>,%(message)s"

logging.basicConfig(
  filename='logs/{}.csv'.format(now), 
  level=logging.INFO, 
  format=LOG_FORMAT,
  datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()

class App:
    def __init__(self):
        self.fs = FsModule()
        self.sc = Scraper()

    def createNewListingData(self):
      """
        1. Get 'NewListings' from db
        2. Scrape data
        3. Create a new Listing Doc
        4. Add the first DataRow Doc to 'data' subcol
        5. Mark created 'NewListing'
      """
      newListingUrls = self.fs.getNewListingURLs()
      newListingCount = len(newListingUrls)

      if(newListingCount > 0) :
        logging.info("Started scraping {} new Listing data...".format(newListingCount))
        i = 1
        for obj in newListingUrls:
          l = self.sc.scrapeInitialListing(obj.url)

          listingDocPath = self.fs.createListing(l.listingName, l.listingID, l.listingURL, l.storeName, l.storeArea)
          self.fs.insertSingleListingDataRow(l.listingID, l.dataRow)
          
          self.fs.setNewListingDocAddr(obj.selfDocAddr, listingDocPath)
          logging.info("Successfully scraped {} of {} (ListingID:{})".format(i,newListingCount,l.listingID))
          i += 1
      else:
        logging.info("No new ListingUrls found")

    def updateListingData(self):
      """
        1. Get all Listing Document from db
        2. Scrape data
        3. create a new DataRow Doc inside each Listing Doc
      """
      listObj = self.fs.getExistingListingURLs()
      countObj = len(listObj)

      if(countObj > 0):
        logging.info("Started updating {} Listing(s)...".format(countObj))

        i = 1
        for obj in listObj:
          dataRow = self.sc.scrapeListingDataRow(obj.listingID)
          self.fs.insertSingleListingDataRow(obj.listingID, dataRow)
          logging.info("Successfully updated {} of {} (ListingID:{})".format(i,countObj,obj.listingID))
          i += 1
      else:
        logging.info("No ExistingListing needs to be updated")

def main():
  app = App()

  app.createNewListingData()
  app.updateListingData()

if __name__ == '__main__':
  main()