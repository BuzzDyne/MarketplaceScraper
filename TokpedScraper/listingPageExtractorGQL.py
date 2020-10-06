import requests

API_ENDPOINT = "https://gql.tokopedia.com/"
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

requestPayload = {
    "operationName":"PDPInfoQuery",
    "variables":{
        "shopDomain":"enterkomputer","productKey":"vga-galax-geforce-gtx-1650-super-4gb-ddr6-ex-1-click-oc-dual-fan"
    },
    "query":"query PDPInfoQuery($shopDomain: String, $productKey: String) {\n  getPDPInfo(productID: 0, shopDomain: $shopDomain, productKey: $productKey) {\n    basic {\n      id\n      shopID\n      name\n      alias\n      price\n      priceCurrency\n      lastUpdatePrice\n      description\n      minOrder\n      maxOrder\n      status\n      weight\n      weightUnit\n      condition\n      url\n      sku\n      gtin\n      isKreasiLokal\n      isMustInsurance\n      isEligibleCOD\n      isLeasing\n      catalogID\n      needPrescription\n      __typename\n    }\n    shopInfo\n    category {\n      id\n      name\n      title\n      breadcrumbURL\n      isAdult\n      detail {\n        id\n        name\n        breadcrumbURL\n        __typename\n      }\n      __typename\n    }\n    pictures {\n      picID\n      fileName\n      filePath\n      description\n      isFromIG\n      width\n      height\n      urlOriginal\n      urlThumbnail\n      url300\n      status\n      __typename\n    }\n    preorder {\n      isActive\n      duration\n      timeUnit\n      __typename\n    }\n    wholesale {\n      minQty\n      price\n      __typename\n    }\n    videos {\n      source\n      url\n      __typename\n    }\n    campaign {\n      campaignID\n      campaignType\n      campaignTypeName\n      originalPrice\n      discountedPrice\n      isAppsOnly\n      isActive\n      percentageAmount\n      stock\n      originalStock\n      startDate\n      endDate\n      endDateUnix\n      appLinks\n      hideGimmick\n      __typename\n    }\n    stats {\n      countView\n      countReview\n      countTalk\n      rating\n      __typename\n    }\n    txStats {\n      txSuccess\n      txReject\n      itemSold\n      itemSoldPaymentVerified\n      __typename\n    }\n    cashback {\n      percentage\n      __typename\n    }\n    variant {\n      parentID\n      isVariant\n      __typename\n    }\n    stock {\n      useStock\n      value\n      stockWording\n      __typename\n    }\n    menu {\n      name\n      __typename\n    }\n    __typename\n  }\n}\n"
}

searchPayload = {
            "operationName":"SearchProductQueryV4",
            "variables":{
                "params":"scheme=https&device=desktop&related=true&st=product&q=GTX&ob=23&page=1&variants=&shipping=&start=0&rows=5&user_id=&unique_id=d2426b563c16fd7b333dff580e431f86&safe_search=false&source=search"
            },
            "query":"query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      __typename\n    }\n    data {\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        shop {\n          id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
        }

r = requests.post(url=API_ENDPOINT, json=requestPayload)

# dataTree = r.json().get('data').get('getPDPInfo')

# print(dataTree.get("basic").get("name"))
# print(dataTree.get("basic").get("price"))
# print(dataTree.get("stock").get("value"))

# print(dataTree.get("txStats").get("itemSoldPaymentVerified"))
# print(dataTree.get("stats").get("countView"))

# print(dataTree.get("stats").get("rating"))
# print(dataTree.get("stats").get("countReview"))

# print(dataTree.get("stats").get("countView")) # Store Name
# print(dataTree.get("stats").get("countView")) # Store Area

file = open("resp_text2.txt", "w")
file.write(r.text)
file.close()