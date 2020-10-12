import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

from prodLists import listingObj 
import myUtil

chrome_path = 'D:\\chromedriver.exe'

searchUrl = 'https://www.tokopedia.com/search?st=product&q='
searchQuery = 'LG TV'

srcResultContainer_xpath    = '//div[@class="css-jza1fo"]'
srcResult_xpath             = '//div[@class="css-1g20a2m"]'
watchEle_xpath              = "//span[@class='css-1bjwylw']"
nextPage_xpath              = "//i[@class='css-98hn3t e19tp72t1']"

watchEleListingPage_xpath   = "//div[@class='css-1gomreu']"

listingName_xpath           = ".//span[@class='css-1bjwylw']"
listingPrice_xpath          = ".//span[@class='css-o5uqvq']"
listingLoc_xpath            = ".//span[@class='css-1kr22w3']"
listingUrl_xpath            = ".//a[@class='css-89jnbj']"

reviewScoreAndCount_xpath   = "//span[@class='css-4g6ai3']/span"
soldCount_xpath             = "//b[@data-testid='lblPDPDetailProductSoldCounter']"
seenCount_xpath             = "//span[@data-testid='lblPDPDetailProductSeenCounter']/b"
listingStore_xpath          = "//a[@class='css-xmjuvc']"

deltaSec = 2 * (3600)

# listingStoreAndLoc_xpath    = ".//div[@class='css-vbihp9']"
# listingLoc_xpath    = ".//span[@class='css-1kr22w3'][1]"
# listingStoreAndLoc_xpath    = ".//span[@class='css-1kr22w3']"1
#css-1kr22w3, first is Loc, Second is StoreName

class ScrapeDriver:

    def startupDriver(self):
        opts = Options()
        # opts.add_argument("--disable-extensions")
        # opts.add_argument("--disable-gpu")
        # opts.add_argument('--no-proxy-server') 
        opts.add_argument("--proxy-server='direct://'")
        opts.add_argument("--proxy-bypass-list=*")
        
        # opts.add_argument("--headless")

        opts.add_experimental_option("excludeSwitches", ["enable-logging"])

        driver = webdriver.Chrome(chrome_path,options=opts, service_log_path='NULL.txt')
        return driver
        
    def __init__(self, useSelenium=False):
        if(useSelenium):
            self.driver = self.startupDriver()

    def openUrl(self, url, watchXpath):
        self.driver.get(url)
        
        try:
            element = WebDriverWait(self.driver, 60).until(\
                EC.presence_of_element_located((By.XPATH, watchXpath)))
        except TimeoutException as e:
            print(e)

    # def goBack(self, watchXpath):
        #     self.driver.back()
        #     # self.driver.execute_script("window.history.go(-1)")
        #     try:
        #         element = WebDriverWait(self.driver, 60).until(\
        #             EC.presence_of_element_located((By.XPATH, watchXpath)))
        #         print("OK")
        #     except TimeoutException as e:
        #         print(e)

    # def getDataFromListingPage(self, pObj):
        #     """Takes listingOBJ, open its link, extract and add listing data directly to the listingOBJ [DEPRECATED]
            
        #     This approach use a Chrome Webdriver to manually load listing page and watch each xPath of data elements, then normalize and later add it to listingOBJ"""
        #     defIntValue = 0
        #     defStrValue = "-"

        #     # pObj.soldCount = 9999
        #     # pObj.seenCount = 9999
        #     # pObj.reviewScore = 9999
        #     # pObj.reviewCount = 9999
        #     # pObj.storeName = "-"

        #     self.openUrl(pObj.listingUrl, watchEleListingPage_xpath)

        #     soldEle = self.driver.find_elements_by_xpath(soldCount_xpath)
        #     seenEle = self.driver.find_elements_by_xpath(seenCount_xpath)
        #     rScoreEle = self.driver.find_elements_by_xpath(reviewScoreAndCount_xpath)
        #     rCountEle = self.driver.find_elements_by_xpath(reviewScoreAndCount_xpath)
        #     sNameEle = self.driver.find_elements_by_xpath(listingStore_xpath)

        #     if (len(soldEle) > 0):
                
        #         pObj.soldCount = myUtil.filterNonNumericToInt(soldEle[0].text)
        #     else:
        #         pObj.soldCount = defIntValue
            
        #     if (len(seenEle) > 0):
        #         pObj.seenCount = myUtil.filterNonNumericToInt(seenEle[0].text)
        #     else:
        #         pObj.seenCount = defIntValue

        #     if (len(rScoreEle) > 0):
        #         pObj.reviewScore = myUtil.filterNonNumericToInt(rScoreEle[0].text)
        #     else:
        #         pObj.reviewScore = defIntValue

        #     if (len(rCountEle) > 0):
        #         pObj.reviewCount = myUtil.filterNonNumericToInt(rCountEle[1].text)
        #     else:
        #         pObj.reviewCount = defIntValue

        #     if (len(sNameEle) > 0):
        #         pObj.storeName = sNameEle[0].text
        #     else:
        #         pObj.storeName = defIntValue

        #     pObj.timestamp = int(time.time())

        #     # pObj.soldCount = self.driver.find_element_by_xpath(soldCount_xpath).text
        #     # pObj.seenCount = self.driver.find_element_by_xpath(seenCount_xpath).text
        #     # pObj.reviewScore = self.driver.find_elements_by_xpath(reviewScoreAndCount_xpath)[0].text
        #     # pObj.reviewCount = self.driver.find_elements_by_xpath(reviewScoreAndCount_xpath)[1].text
        #     # pObj.storeName = self.driver.find_element_by_xpath(listingStore_xpath).text

    def getDataFromListingPageBS(self, pObj, header=None):
        """Takes listingOBJ, open its link, extract and add listing data directly to the listingOBJ
        
        This approach use Requests module to get listing page's HTML and extract data using BeautifulSoup4, then normalize and later add it to listingOBJ"""
        defIntValue = 0

        if(header == None):
            header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
            }
        
        page = requests.get(pObj.listingUrl, headers=header)
        soup = BeautifulSoup(page.text, 'html.parser')

        lblListingName  = {'data-testid' : 'lblPDPDetailProductName'}
        lblListingPrice = {'data-testid' : 'lblPDPDetailProductPrice'}
        lblListingStock = {'data-testid' : 'lblPDPDetailProductStock'}

        lblSoldCount    = {'data-testid' : 'lblPDPDetailProductSuccessRate'}
        lblSeenCount    = {'data-testid' : 'lblPDPDetailProductSeenCounter'}
        
        lblReviewScore  = {'data-testid' : 'lblPDPDetailProductRatingNumber'}
        lblReviewCount  = {'data-testid' : 'lblPDPDetailProductRatingCounter'}
        
        lblStoreName    = {'data-testid' : 'llbPDPFooterShopName'}
        lblStoreArea    = {'data-testid' : 'lblPDPFooterLastOnline'}

        
        listingNameText = soup.find(attrs=lblListingName)
        listingPriceText= soup.find(attrs=lblListingPrice)
        listingStockText= soup.find(attrs=lblListingStock)

        soldCountText   = soup.find(attrs=lblSoldCount)
        seenCountText   = soup.find(attrs=lblSeenCount)
        
        reviewScoreText = soup.find(attrs=lblReviewScore)
        reviewCountText = soup.find(attrs=lblReviewCount)
        
        storeNameText   = soup.find(attrs=lblStoreName)
        storeaAreaText  = soup.find(attrs=lblStoreArea)

        # Listing Name
        if(listingNameText is None):
            pObj.nameProd = "NoneType"
        else:
            pObj.nameProd = listingNameText.get_text()

        # Listing Price
        if(listingPriceText is None):
            pObj.priceProd = defIntValue
        else:
            pObj.priceProd = myUtil.filterNonNumericToInt(listingPriceText.get_text()) 

        # Stock
        if(listingStockText is None):
            pObj.listingStock = -1                              #NoneType
        else:
            stock = listingStockText.get_text()
            if("kosong" in stock):
                pObj.listingStock = 0                                   #Empty
            elif("terakhir" in stock):
                pObj.listingStock = 1                                   #LastStock
            elif(stock == ""):
                pObj.listingStock = 9999                                #Many
            else:
                pObj.listingStock = myUtil.filterNonNumericToInt(stock) #Limited

        # Sold Count
        if(soldCountText is None):
            pObj.soldCount = defIntValue
        else:
            pObj.soldCount = myUtil.filterNonNumericToInt(soldCountText.get_text())

        # Seen Count
        if(seenCountText is None):
            pObj.seenCount = defIntValue
        else:
            pObj.seenCount = myUtil.filterNonNumericToInt(seenCountText.get_text())
        
        # Review Score
        if(reviewScoreText is None):
            pObj.reviewScore = defIntValue
        else:
            pObj.reviewScore = myUtil.filterNonNumericToInt(reviewScoreText.get_text())
        
        # Review Count
        if(reviewCountText is None):
            pObj.reviewCount = defIntValue
        else:
            pObj.reviewCount = myUtil.filterNonNumericToInt(reviewCountText.get_text())

        # Store Name
        if(storeNameText is None):
            pObj.storeName = "NoneType"
        else:
            pObj.storeName = storeNameText.get_text()

        # Store Area
        if(storeaAreaText is None):
            pObj.storeArea = "NoneType"
        else:
            pObj.storeArea = myUtil.shopAreaCleaner(storeaAreaText.get_text())

        pObj.timestamp = int(time.time() - deltaSec)

    # def scrapeProduct(self, productQuery):
        #     self.openUrl(searchUrl+productQuery, watchEle_xpath)

        #     products = self.driver.find_elements_by_xpath(srcResult_xpath)

        #     pList = []

        #     # Extract listing data available from search page (Name, Price, Area, Url) and append ListingObj to listingObjList
        #     for p in products:
        #         pName = p.find_element_by_xpath(listingName_xpath).text
        #         pPrice = p.find_element_by_xpath(listingPrice_xpath).text
        #         pArea = p.find_element_by_xpath(listingLoc_xpath).text
        #         pUrl = p.find_element_by_xpath(listingUrl_xpath).get_attribute('href')

        #         # pPrice = int(sub(r'[^0-9]', '', pPrice))

        #         pPrice = myUtil.filterNonNumericToInt(pPrice)

        #         pList.append(listingObj(nameProd=pName, priceProd=pPrice, storeArea=pArea, listingUrl=pUrl))
        #         print(".", end="")

        #     print("")
            
        #     # Get the rest of missing listing data by visiting each listingUrl
        #     for p in pList:
        #         self.getDataFromListingPage(p)
        #         print(".", end="")
            
        #     print("")

        #     return pList
        #     # for p in pList:
        #     #     p.toString()

    # def scrapeProductBS(self, productQuery, header=None):
        #     """
        #         Get listing data from search result page with BS4 and Requests

        #         Initially only gets URL of each listing and then calls getDataFromListingPageBS() to scrape the rest of the data from every listing page from URL previously stored per listing.
        #     """
        #     if(header == None):
        #         header = {
        #             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        #         }

        #     lblListingCard = {'data-testid' : "lnkProductContainer"}
            
        #     page = requests.get(searchUrl+productQuery, headers=header)
        #     soup = BeautifulSoup(page.text, 'html.parser')

        #     # Create list of listingObj with only its own URL
        #     pList = []
        #     for a in soup.find_all(attrs=lblListingCard):
        #         pList.append(listingObj(listingUrl=a['href']))
        #         print(".", end="")
        #     print("")

        #     # Fetch the rest of listing data with its url
        #     for p in pList:
        #         self.getDataFromListingPageBS(p)
        #         print(".", end="")
        #     print("")

        #     return pList

    def scrapeProductGQL(self, productQuery=None, header=None, nListing=None):
        """
            Get listing data from Tokopedia's GraphQL endpoint (JSON)

            Initially only gets URL and listingID of each listing and then calls getDataFromListingPageBS() to scrape the rest of the data from every listing page from URL previously stored per listing.
        """
        API_ENDPOINT = "https://gql.tokopedia.com/"

        if(productQuery == None):
            print("Inside scrapeProductGQL: productQuery is None type")
            return -1

        if(header == None):
            header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
            }

        if(nListing == None):
            nListing = 60

        requestPayload = {
            "operationName":"SearchProductQueryV4",
            "variables":{
                "params":"scheme=https&device=desktop&related=true&st=product&q={}&ob=23&page=1&variants=&shipping=&start=0&rows={}&user_id=&unique_id=d2426b563c16fd7b333dff580e431f86&safe_search=false&source=search".format(productQuery,nListing)
            },
            "query":"query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    data {\n      products {\n        id\n        name\n        ads {\n          id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        shop {\n          id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
        }

        r = requests.post(url = API_ENDPOINT, json=requestPayload)
        
        dataTree = r.json().get('data').get('ace_search_product_v4').get('data').get('products')

        # Create list of listingObj with only its own URL and listingID
        pList = []
        for x in dataTree:
            pList.append(listingObj(listingUrl=x.get('url'), listingID=x.get('id')))
            print(".", end="")
        print("")

        # Fetch the rest of listing data with its url
        for p in pList:
            self.getDataFromListingPageBS(p)
            print(".", end="")
        print("")

        return pList

    def processQuery(self, qName):
        pList = self.scrapeProductGQL(qName, nListing=10)
        myUtil.writeToCSV(qName, pList, time.time() - deltaSec)

    def processListOfQuery(self, listQ):
        for p in listQ:
            self.processQuery(p)

d = ScrapeDriver(useSelenium=False)

vgaList = [     "GTX 1650",
                "GTX 1650 Super",
                "GTX 1660",
                "GTX 1660 Ti",
                "GTX 1660 Super",
                "GTX 1080",
                "RTX 2060",
                "RTX 2060 Super",
                "RTX 2070",
                "RTX 2070 Super",
                "RTX 2080",
                "RTX 2080 Ti",
                "RTX 2080 Super",
                "RX 5700 XT",
                "RX 5700",
                "RX 5600 XT",
                "RX 5600",
                "RX 5500 XT",
                "RX 5500"]

cpuList = [     "Ryzen 5 3600",
                "Ryzen 5 3600X",
                "Ryzen 5 2600X",
                "Ryzen 3 3300X",
                "Ryzen 3 2200G",
                "i9 9900K",
                "i5 9600K"]

start = time.time()

d.processListOfQuery(vgaList)
d.processListOfQuery(cpuList)

end = time.time()
print("Time: {}".format(end - start))
