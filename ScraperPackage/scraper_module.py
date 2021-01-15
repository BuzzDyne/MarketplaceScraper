import requests
from bs4 import BeautifulSoup

from DataModel.listingObj import ListingObj
from DataModel.fs_package_model import ListingDataRow

from ScraperPackage import utils
from ScraperPackage.scraper_status_code import ScraperStatusCode as STATUS

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
  
    def scrapeInitialListing(self, listingUrl):
        """Returns a ListingObj containing scraped data from a given ListingUrl
        
        - Called when writing a new Listing Doc
        - listingUrl must be in this format 'tokopedia.com/SHOP_DOMAIN/PRODUCT_KEY' 
        - If Listing is not found, returns ListingObj with ListingID of None
        """
        # https://www.tokopedia.com/supergamingid/intel-core-i5-10400f-coffee-lake-promo-gaming-murah

        if listingUrl is None:
            return ListingObj(None)

        x = listingUrl.split('/')
        productKey = x[-1]
        shopDomain = x[-2]

        byUrlPayload = {
            "operationName":"PDPInfoQuery",
            "variables":{
                "shopDomain" : shopDomain,
                "productKey" : productKey
            },
            "query": """
            query PDPInfoQuery($shopDomain:String, $productKey:String) {
                getPDPInfo(productID:0,shopDomain:$shopDomain,productKey:$productKey) {
                    basic {
                        id
                        shopID
                        name
                        alias
                        price
                        lastUpdatePrice
                        status
                        url
                    }
                    stats {
                        countView
                        countReview
                        rating
                    }
                    txStats {
                        itemSold
                    }
                    campaign{
                        discountedPrice
                        isActive
                    }
                    stock {
                        useStock
                        value
                        stockWording
                    }
                    pictures {
                        urlOriginal 
                        urlThumbnail
                    }
                }
            }
            """
        }

        r = requests.post(url= API_ENDPOINT, json=byUrlPayload)

        if r.json()['data'] is None:
            return ListingObj(None)
        else:
            dataTree = r.json()['data']['getPDPInfo']

            isDiscounted = dataTree['campaign']['isActive']

            res = ListingObj()

            res.listingName     = dataTree['basic']['name']
            res.listingID       = str(dataTree['basic']['id'])
            res.listingURL      = listingUrl
            res.listingImgURL   = dataTree['pictures'][0]['urlOriginal']
            res.listingThumbURL = dataTree['pictures'][0]['urlThumbnail']
            res.storeName       = self.getShopNameByDomain(shopDomain)
            # res.storeArea     = xxxx

            sold            = dataTree['txStats']['itemSold']
            seen            = dataTree['stats']['countView']
            stock           = dataTree['stock']['value']
            reviewCount     = dataTree['stats']['countReview']
            reviewScore     = dataTree['stats']['rating']
            price           = dataTree['campaign']['discountedPrice'] if isDiscounted else dataTree['basic']['price']

            res.setDataRow(sold,seen,stock,reviewCount,reviewScore,price)

            return res
    
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

    def scrapeListingDataRow(self, listingID):
        """Returns a ListingDataRow of a Listing given its ListingID
        
        ListingDataRow have a field named 'statusCode' to indicate the result of the request"""

        byProductID = {
            "operationName":"PDPInfoQuery",
            "variables":{
                "productID" : int(listingID)
            },
            "query": """
            query PDPInfoQuery($productID:Int){
                getPDPInfo(productID:$productID) {
                    basic {
                        price
                        lastUpdatePrice
                        status
                    }
                    stats {
                        countView
                        countReview
                        rating
                    }
                    txStats {
                        itemSold
                    }
                    campaign{
                        discountedPrice
                        isActive
                    }
                    stock {
                        useStock
                        value
                    }
                }
            }
            """
        }

        r = requests.post(url= API_ENDPOINT, json=byProductID)

        # ScrapeListing Error Handling
        if(r.json()['data'] == None):
            # Product Not Found
            if('2001410' in r.json()['errors'][0]['message']):
                return ListingDataRow(statusCode=STATUS.PRODUCT_NOT_FOUND)

            return ListingDataRow(statusCode=STATUS.UNKNOWN_ERROR)

        dataTree = r.json()['data']['getPDPInfo']

        isDiscounted = dataTree['campaign']['isActive']

        res = ListingDataRow()

        res.sold            = dataTree['txStats']['itemSold']
        res.seen            = dataTree['stats']['countView']
        res.stock           = dataTree['stock']['value']
        res.reviewCount     = dataTree['stats']['countReview']
        res.reviewScore     = dataTree['stats']['rating']
        res.price           = dataTree['campaign']['discountedPrice'] if isDiscounted else dataTree['basic']['price']

        return res
