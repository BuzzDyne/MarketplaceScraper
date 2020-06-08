import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

from prodLists import ProdList

chrome_path = 'D:\\chromedriver.exe'

searchUrl = 'https://www.tokopedia.com/search?st=product&q='
searchQuery = 'LG TV'

srcResultContainer_xpath    = '//div[@class="css-jza1fo"]'
srcResult_xpath             = '//div[@class="css-1g20a2m"]'
watchEle_xpath              = "//span[@class='css-1bjwylw']"
nextPage_xpath              = "//i[@class='css-98hn3t e19tp72t1']"

listingName_xpath           = ".//span[@class='css-1bjwylw']"
listingPrice_xpath          = ".//span[@class='css-o5uqvq']"
listingLoc_xpath            = ".//span[@class='css-1kr22w3']"
listingPage_xpath           = ".//a[@class='css-89jnbj']"

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

    def scrapeProduct(self, productQuery):
        self.driver.openUrl(searchUrl+productQuery, watchEle_xpath)

d = ScrapeDriver()


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