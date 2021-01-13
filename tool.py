import logging
from datetime import datetime, timedelta
import pytz
import requests
import json
from ScraperPackage.scraper_module import Scraper
from FsPackage.fs_module import FsModule
from DataModel.fs_package_model import ListingDataRow, ExistingListingObj, NewListingUrl
import sys

API_ENDPOINT = "https://gql.tokopedia.com/"
q = """ query PDPInfoQuery($productID:Int){
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
                    stock {
                        useStock
                        value
                    }
                }
            } """
oriQ = """ query PDPInfoQuery($productID:Int) {
    getPDPInfo(productID:$productID) {
        basic {
            id 
            shopID 
            name 
            alias 
            price 
            priceCurrency
            lastUpdatePrice 
            description 
            minOrder 
            maxOrder 
            status 
            weight 
            weightUnit 
            condition 
            url 
            sku 
            gtin 
            isKreasiLokal 
            isMustInsurance 
            isEligibleCOD 
            isLeasing 
            catalogID 
            needPrescription
        }
        category {
            id 
            name 
            title 
            breadcrumbURL 
            isAdult 
            detail {id name breadcrumbURL}
        }
        pictures {
            picID 
            fileName 
            filePath 
            description 
            isFromIG 
            width 
            height 
            urlOriginal 
            urlThumbnail 
            url300 
            status
        }
        preorder{
            isActive duration timeUnit
        }
        wholesale{
            minQty price
        }
        videos{
            source url
        }
        campaign{
            campaignID 
            campaignType 
            campaignTypeName 
            originalPrice 
            discountedPrice 
            isAppsOnly 
            isActive 
            percentageAmount 
            stock 
            originalStock 
            startDate 
            endDate 
            endDateUnix 
            appLinks 
            hideGimmick
        }
        stats{
            countView 
            countReview 
            countTalk 
            rating
        }
        txStats{
            txSuccess 
            txReject 
            itemSold 
            itemSoldPaymentVerified
        }
        cashback{
            percentage
        }
        variant{parentID isVariant}
        stock{useStock value stockWording}
        menu{name}}} """
promoQ = """ query PDPInfoQuery($productID:Int) {
    getPDPInfo(productID:$productID) {
        basic {
            id 
            shopID 
            name 
            alias 
            price 
            priceCurrency
            lastUpdatePrice  
            minOrder 
            maxOrder 
            status 
            weight 
            weightUnit 
            condition 
            url 
            sku 
            gtin 
            isKreasiLokal 
            isMustInsurance 
            isEligibleCOD 
            isLeasing 
            catalogID 
            needPrescription
        }
        campaign{
            campaignID 
            campaignType 
            campaignTypeName 
            originalPrice 
            discountedPrice 
            isAppsOnly 
            isActive 
            percentageAmount 
            stock 
            originalStock 
            startDate 
            endDate 
            endDateUnix 
            appLinks 
            hideGimmick
        }
        stock{useStock value stockWording}
    }}"""
picQ = """ query PDPInfoQuery($productID:Int) {
    getPDPInfo(productID:$productID) {
        basic {
            id 
            shopID 
            name 
        }
        pictures {
            urlOriginal 
            urlThumbnail
        }
    }}"""


class Tool:
    def __init__(self):
        self.fs = FsModule()

    def addImageURLToExistingListing(self):
        # Get all Exisiting Listing DocID and URL
        listOfListing = self.fs.getAllExistingListingURLs()
        
        # For each Listing
        i = 1
        for listing in listOfListing:
            # Retrieve ImageURL
            imgUrl, thumbUrl = self.getListingImgAndThumbUrl(listing.toDict()['listingID'])
            print(f'Listing Addr ({listing.toDict()["docAddr"]})\nimgUrl: {imgUrl}\nthumbUrl: {thumbUrl}\n\n')

            # Save to DB
            self.fs.updateListingWithImgUrls(listing.toDict()["docAddr"], imgUrl, thumbUrl)

    def getListingImgAndThumbUrl(self, listingID):
        byProductID = {
            "operationName":"PDPInfoQuery",
            "variables":{
                "productID" : listingID
            },
            "query": picQ
        }

        r = requests.post(url=API_ENDPOINT, json=byProductID)

        try:
            dataTree = r.json()['data']['getPDPInfo']
        except TypeError:
            print("TypeError: r.json() : {}".format(r.json()))
        except:
            print("Unexpected error:", sys.exc_info()[0])

        imgUrl  = dataTree["pictures"][0]["urlOriginal"]
        thumbUrl= dataTree["pictures"][0]["urlThumbnail"]

        # return {
        #     'imgUrl': imgUrl,
        #     'thumbUrl': thumbUrl
        # }

        return imgUrl,thumbUrl

    def printPDPInfoByURL(self, listingURL):
        
        def getListingIDbyURL(listingURL):
            x = listingURL.split('/')
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
                        stock {
                            useStock
                            value
                            stockWording
                        }
                        pictures {
                            url300
                        }
                    }
                }
                """
            }

            r = requests.post(url= API_ENDPOINT, json=byUrlPayload)
            dataTree = r.json()['data']['getPDPInfo']

            return dataTree['basic']['id']
        
        listingID = getListingIDbyURL(listingURL)

        byProductID = {
                "operationName":"PDPInfoQuery",
                "variables":{
                    "productID" : listingID
                },
                "query": promoQ
            }
        
        r = requests.post(url=API_ENDPOINT, json=byProductID)
        dataTree = r.json()['data']['getPDPInfo']

        print(json.dumps( dataTree, indent=2))

