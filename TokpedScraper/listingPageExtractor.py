# Extract Data from a listing given the link
# Speed     :   Around 1 Second
# 
# Method    :   - Get the raw HTML file with Requests
#               - Process HTML with BS4
#               - Extract data (Based on Tag's Attribute Name and Value)
#               - Print data to log
# 
# Todo      :   - Error handling when data is not available (NoneType)
#               - Output data to a Data Model
#               - Possible to get IP-Blocked?

import requests
from bs4 import BeautifulSoup

def getListingDataTokped(url, header=None):
    """ Takes Listing Url and returns all listing data in [format] format."""

    if(header == None):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }

    page = requests.get(url, headers=headers)
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

    a = soup.find(attrs=lblListingName).get_text()
    b = soup.find(attrs=lblListingPrice).get_text()
    c = soup.find(attrs=lblListingStock).get_text()

    d = soup.find(attrs=lblSoldCount)
    e = soup.find(attrs=lblSeenCount)
    f = soup.find(attrs=lblReviewScore)
    g = soup.find(attrs=lblReviewCount)
    soup.find_all()
    if(d is None):
        d = "-"
    else:
        d = d.get_text()

    if(e is None):
        e = "-"
    else:
        e = e.get_text()

    if(f is None):
        f = "-"
    else:
        f = f.get_text()

    if(g is None):
        g = "-"
    else:
        g = g.get_text()


    h = soup.find(attrs=lblStoreName).get_text()
    i = soup.find(attrs=lblStoreArea).get_text()

    if("kosong" in c):
        c = "Empty"
    elif(c == ""):
        c = "Available"
    else:
        c = "Limited"

    print("a: {}".format(a))
    print("b: {}".format(b))
    print("c: {}".format(c))
    print("d: {}".format(d))
    print("e: {}".format(e))
    print("f: {}".format(f))
    print("g: {}".format(g))
    print("h: {}".format(h))
    print("i: {}".format(i))

urlList = []
urlList.append('https://www.tokopedia.com/nanokomputer/vga-zotac-gaming-geforce-rtx-2070-super-air-rtx2070-super-8gb-gddr6')
urlList.append('https://www.tokopedia.com/nanokomputer/memory-g-skill-f4-4000c15d-16gtrg-trident-z-royal-16gb-2x8-ddr4-4000')
urlList.append('https://www.tokopedia.com/tokorrj/safety-respirator-reusable-washable-n95')
urlList.append('https://www.tokopedia.com/enterkomputer/galax-geforce-rtx-2070-super-ex-8gb-ddr6-1-click-oc-rgb-effect')

for url in urlList:
    getListingDataTokped(url)

a = "•"