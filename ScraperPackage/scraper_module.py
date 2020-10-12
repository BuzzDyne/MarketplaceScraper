import requests
from bs4 import BeautifulSoup

from DataModel.scraper_package_model import ListingObj

from ScraperPackage import utils

# 1. Need to scrape listing given its Listing URL
    # Problem:
        # ListingID were got from GQL Search Query
            # Must find the GQL Operation Query name to get product data

DEF_INT_VALUE = 0
API_ENDPOINT = "https://gql.tokopedia.com/"

class Scraper:
    def __init__(self):
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }

    def scrapeListingPageBS(self, listingUrl):
        """Returns a ListingObj with all Listing Data (except ListingID) given the URL of the Listing"""

        pObj = ListingObj(listingUrl=listingUrl)

        page = requests.get(listingUrl, headers=self.header)
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

        # Error Handlings
        # Listing Name
        if(listingNameText is None):
            pObj.listingName = "NoneType"
        else:
            pObj.listingName = listingNameText.get_text()

        # Listing Price
        if(listingPriceText is None):
            pObj.priceProd = DEF_INT_VALUE
        else:
            pObj.priceProd = utils.filterNonNumericToInt(listingPriceText.get_text()) 

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
                pObj.listingStock = utils.filterNonNumericToInt(stock) #Limited

        # Sold Count
        if(soldCountText is None):
            pObj.soldCount = DEF_INT_VALUE
        else:
            pObj.soldCount = utils.filterNonNumericToInt(soldCountText.get_text())

        # Seen Count
        if(seenCountText is None):
            pObj.seenCount = DEF_INT_VALUE
        else:
            pObj.seenCount = utils.filterNonNumericToInt(seenCountText.get_text())
        
        # Review Score
        if(reviewScoreText is None):
            pObj.reviewScore = DEF_INT_VALUE
        else:
            pObj.reviewScore = utils.filterNonNumericToInt(reviewScoreText.get_text())
        
        # Review Count
        if(reviewCountText is None):
            pObj.reviewCount = DEF_INT_VALUE
        else:
            pObj.reviewCount = utils.filterNonNumericToInt(reviewCountText.get_text())

        # Store Name
        if(storeNameText is None):
            pObj.storeName = "NoneType"
        else:
            pObj.storeName = storeNameText.get_text()

        # Store Area
        if(storeaAreaText is None):
            pObj.storeArea = "NoneType"
        else:
            pObj.storeArea = utils.shopAreaCleaner(storeaAreaText.get_text())

        return pObj
        
    def scrapeListingUrlGQL(self, listingUrl):
        """Returns a ListingObj containing scraped data from a given ListingUrl"""
        # https://www.tokopedia.com/supergamingid/intel-core-i5-10400f-coffee-lake-promo-gaming-murah
        x = listingUrl.split('/')
        productKey = x[-1]
        shopDomain = x[-2]

        byUrlPayload = {
            "operationName":"PDPInfoQuery",
            "variables":{
                "shopDomain" : shopDomain,
                "productKey" : productKey
            },
            "query": "query PDPInfoQuery($shopDomain:String, $productKey:String){\n  getPDPInfo(productID:0,shopDomain:$shopDomain,productKey:$productKey) {\n  basic {id\n    shopID\n    name\n    alias\n    price\n    lastUpdatePrice\n    status\n    url} stats{\n countView\n countReview\n rating\n} txStats{\n txSuccess\n txReject\n itemSold\n itemSoldPaymentVerified\n} stock{\n useStock\n value\n stockWording\n}  }}"
        }

        r = requests.post(url= API_ENDPOINT, json=byUrlPayload)
        dataTree = r.json()['data']['getPDPInfo']

        res = ListingObj()

        res.listingName = dataTree['basic']['name']
        res.listingID   = dataTree['basic']['id']
        res.listingUrl  = listingUrl
        res.storeName   = self.getShopNameByDomain(shopDomain)
        # res.storeArea   =

        res.priceProd   = dataTree['basic']['price']
        
    def getShopNameByDomain(self, shopDomain):
        """Return a str of ShopName given the shopDomain"""
        shopInfoQuery = {
            "operationName":"PDPShopInfoQuery",
            "variables":{
                "fields" : "",
                "domain" : shopDomain
            },
            # "query": "query PDPShopInfoQuery($shopID:Int){shopInfoByID(input:{shopIDs:$shopID}) {\n  result{\n  shopCore{\n  name\n domain\n  url\n  description\n}  }}",
            "query": """
            query PDPShopInfoQuery ($fields:[String!]!,$domain:String){
                shopInfoByID(input:{shopIDs:[0],fields:$fields,domain:$domain}){
                result {
                    shopCore {
                    name
                    url
                    domain
                    description
                    }
                }
                }
            }
            """
        }

        r = requests.post(url = API_ENDPOINT, json=shopInfoQuery)
        dataTree = r.json()

        return dataTree['data']['shopInfoByID']['result'][0]['shopCore']['name']