import requests
from bs4 import BeautifulSoup

# 1. Need to scrape listing given its Listing URL

class Scraper:
    def __init__(self):
        return

    def scrapeListingPage(self, listingUrl):
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }

        page = requests.get(listingUrl, headers=header)
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

        