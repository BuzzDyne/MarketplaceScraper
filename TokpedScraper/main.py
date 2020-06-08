import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

from prodLists import prodObj 

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

        driver = webdriver.Chrome(chrome_path,options=opts, service_log_path='NULL')
        return driver
        
    def __init__(self):
        self.driver = self.startupDriver()

    def openUrl(self, url, watchXpath):
        self.driver.get(url)
        
        try:
            element = WebDriverWait(self.driver, 60).until(\
                EC.presence_of_element_located((By.XPATH, watchXpath)))
        except TimeoutException as e:
            print(e)

    def goBack(self, watchXpath):
        self.driver.back()
        # self.driver.execute_script("window.history.go(-1)")

        try:
            element = WebDriverWait(self.driver, 60).until(\
                EC.presence_of_element_located((By.XPATH, watchXpath)))
            
            print("OK")
        except TimeoutException as e:
            print(e)

    def getDataFromListingPage(self, pObj):
        defIntValue = 0
        defStrValue = "-"

        # pObj.soldCount = 9999
        # pObj.seenProduct = 9999
        # pObj.reviewScore = 9999
        # pObj.reviewCount = 9999
        # pObj.storeName = "-"

        self.openUrl(pObj.listingUrl, watchEleListingPage_xpath)

        soldEle = self.driver.find_elements_by_xpath(soldCount_xpath)
        seenEle = self.driver.find_elements_by_xpath(seenCount_xpath)
        rScoreEle = self.driver.find_elements_by_xpath(reviewScoreAndCount_xpath)
        rCountEle = self.driver.find_elements_by_xpath(reviewScoreAndCount_xpath)
        sNameEle = self.driver.find_elements_by_xpath(listingStore_xpath)

        if (len(soldEle) > 0):
            pObj.soldCount = soldEle[0].text
        else:
            pObj.soldCount = defIntValue
        
        if (len(seenEle) > 0):
            pObj.seenProduct = seenEle[0].text
        else:
            pObj.seenProduct = defIntValue

        if (len(rScoreEle) > 0):
            pObj.reviewScore = rScoreEle[0].text
        else:
            pObj.reviewScore = defIntValue

        if (len(rCountEle) > 0):
            pObj.reviewCount = rCountEle[1].text
        else:
            pObj.reviewCount = defIntValue

        if (len(sNameEle) > 0):
            pObj.storeName = sNameEle[0].text
        else:
            pObj.storeName = defIntValue

        # pObj.soldCount = self.driver.find_element_by_xpath(soldCount_xpath).text
        # pObj.seenProduct = self.driver.find_element_by_xpath(seenCount_xpath).text
        # pObj.reviewScore = self.driver.find_elements_by_xpath(reviewScoreAndCount_xpath)[0].text
        # pObj.reviewCount = self.driver.find_elements_by_xpath(reviewScoreAndCount_xpath)[1].text
        # pObj.storeName = self.driver.find_element_by_xpath(listingStore_xpath).text

    def scrapeProduct(self, productQuery):
        self.openUrl(searchUrl+productQuery, watchEle_xpath)

        products = self.driver.find_elements_by_xpath(srcResult_xpath)

        pList = []

        for p in products:
            pName = p.find_element_by_xpath(listingName_xpath).text
            pPrice = p.find_element_by_xpath(listingPrice_xpath).text
            pArea = p.find_element_by_xpath(listingLoc_xpath).text
            pUrl = p.find_element_by_xpath(listingUrl_xpath).get_attribute('href')

            pList.append(prodObj(nameProd=pName, priceProd=pPrice, storeArea=pArea, listingUrl=pUrl))
            print(".", end="")

        for p in pList:
            self.getDataFromListingPage(p)
            print(".", end="")
        
        for p in pList:
            p.toString()



d = ScrapeDriver()

d.scrapeProduct("2060 Super")

d.scrapeProduct("2070 Super")

d.scrapeProduct("1660 Super")

# d.openUrl(searchUrl+searchQuery,watchEle_xpath)
# products = d.driver.find_elements_by_xpath(srcResult_xpath)

# for p in products:

#     pName = p.find_element_by_xpath(listingName_xpath).text
#     pPrice = p.find_element_by_xpath(listingPrice_xpath).text
#     pArea = p.find_element_by_xpath(listingLoc_xpath).text

#     print("Name: " + pName)
#     print("Price: " + pPrice)
#     print("Area: " + pArea)
    
#     p.click()

#     time.sleep(3)

#     pStore = d.driver.find_element_by_xpath(listingStore_xpath).text
#     print("Store: " + pStore)

#     d.driver.back()
#     time.sleep(3)
#     print("-------------------")
#     # for x in p.find_elements_by_xpath(listingStoreAndLoc_xpath):
#     #     print(x.text)


# i = 1
# for p in products:
#     print("\n\n{}".format(i))
#     print(p.text)
#     i += 1