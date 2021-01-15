import logging
from datetime import datetime, timedelta
import pytz

from ScraperPackage.scraper_module import Scraper
from ScraperPackage.scraper_status_code import ScraperStatusCode as STATUS
from FsPackage.fs_module import FsModule
from FsPackage.scraper_enum import ScraperStatusCode as SC

logFileName = datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime("%Y-%m")
LOG_FORMAT = "%(levelname)s,%(asctime)s.%(msecs)03d,%(module)s<%(funcName)s>,%(message)s"

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
      logging.basicConfig(
        filename='logs/create/{}.csv'.format(logFileName), 
        level=logging.INFO, 
        format=LOG_FORMAT,
        datefmt='%Y-%m-%d %H:%M:%S')
      logger = logging.getLogger()

      newListingUrls = self.fs.getNewListingURLs()
      newListingCount = len(newListingUrls)

      if(newListingCount > 0) :
        logging.info("Started scraping {} new Listing data...".format(newListingCount))
        i = 1
        for obj in newListingUrls:
          lObj = self.sc.scrapeInitialListing(obj.url)

          # (NOT_FOUND Check)
          if lObj.listingID is None:
            self.fs.setNewListingDocAddr(obj.selfDocAddr, None, SC.NOT_FOUND)
            logging.info("Listing Not Found -- {} of {} (ListingURL:{})".format(i,newListingCount,obj.url))
            continue

          # (EXISTED Check)
          listingDocPath = self.fs.getListingDocAddrByID(lObj.listingID)
          if listingDocPath is not None:

            # Direct to existed Listing
            self.fs.setNewListingDocAddr(obj.selfDocAddr, listingDocPath, SC.EXISTED)
            logging.info("Listing has existed  {} of {} (ListingDocPath:{})".format(i,newListingCount,listingDocPath))

            # For each User, set activeTracking's startData to latestDatarow
            users_uid = obj.users

            # Remove 'admin' from list
            try:
              users_uid.remove("admin")
            except ValueError:
              pass

            # Get ListingData and its latestDataRow
            listingDocID = listingDocPath.split('/')[-1]
            latestDataRow = self.fs.getListingLatestDataRowByAddr(listingDocPath)
            listingObj = self.fs.getListingObjByAddr(listingDocPath)
            listingObj.setDataRowByObj(latestDataRow)

            userCount = len(users_uid)
            logging.info("Found {} user to be processed...".format(userCount))
            i = 1
            for uid in users_uid:
              self.fs.createTracking(uid, listingObj, listingDocID)
              logging.info("Processed user doc - {} of {} (uid:{})".format(i, userCount, uid))
              i += 1
          # CREATED
          else:
            listingDocPath = self.fs.createListing(lObj)
            self.fs.insertSingleListingDataRow(lObj.listingID, lObj.dataRow)

            self.fs.setNewListingDocAddr(obj.selfDocAddr, listingDocPath, SC.CREATED)
            logging.info("Successfully scraped {} of {} (ListingID:{})".format(i, newListingCount, lObj.listingID))

            # For each User, set activeTracking's startData to latestDatarow
            users_uid = obj.users

            # Remove 'admin' from list
            try:
              users_uid.remove("admin")
            except ValueError:
              pass

            # Get ListingData and its latestDataRow
            listingDocID = listingDocPath.split('/')[-1]
            latestDataRow = self.fs.getListingLatestDataRowByAddr(listingDocPath)
            listingObj = self.fs.getListingObjByAddr(listingDocPath)
            listingObj.setDataRowByObj(latestDataRow)

            userCount = len(users_uid)
            logging.info("Found {} user to be processed...".format(userCount))
            i = 1
            for uid in users_uid:
              self.fs.createTracking(uid, listingObj, listingDocID)
              logging.info("Processed user doc - {} of {} (uid:{})".format(i, userCount, uid))
              i += 1

        i += 1
      else:
        logging.info("No new ListingUrls found")

    def updateListingData(self):
      """
        1. Get all Listing Document from db
        2. Scrape data
        3. create a new DataRow Doc inside each Listing Doc
      """

      logging.basicConfig(
        filename='logs/update/{}.csv'.format(logFileName), 
        level=logging.INFO, 
        format=LOG_FORMAT,
        datefmt='%Y-%m-%d %H:%M:%S')
      logger = logging.getLogger()

      listObj = self.fs.getExistingListingURLs()
      countObj = len(listObj)

      if(countObj > 0):
        logging.info("Started updating {} Listing(s)...".format(countObj))

        i = 1
        for obj in listObj:
          dataRow = self.sc.scrapeListingDataRow(obj.listingID)

          if dataRow.statusCode is STATUS.SUCCESS:
            self.fs.insertSingleListingDataRow(obj.listingID, dataRow)
            logging.info("Successfully updated {} of {} (ListingID:{})".format(i,countObj,obj.listingID))

          elif dataRow.statusCode is STATUS.PRODUCT_NOT_FOUND:
            # TODO implement Listing Status and make it "Deleted" if product is no longer being listed
            logging.info("Listing is not found {} of {} (ListingID:{})".format(i,countObj,obj.listingID))

          else:
            logging.info("Unknown error occurs {} of {} (ListingID:{})".format(i,countObj,obj.listingID))

          i += 1
      else:
        logging.info("No ExistingListing needs to be updated")

def create():
  app = App()
  app.createNewListingData()

def update():
  app = App()
  app.updateListingData()
