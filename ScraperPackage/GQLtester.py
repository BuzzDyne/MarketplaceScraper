import requests

API_ENDPOINT = "https://gql.tokopedia.com/"

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

"""
query SearchProductQueryV4($params: String!) {
  ace_search_product_v4(params: $params) {
    header {
      totalData
      totalDataText
      processTime
      responseCode
      errorMessage
      additionalParams
      keywordProcess
      __typename
    }
    data {
      isQuerySafe
      ticker {
        text
        query
        typeId
        __typename
      }
      redirection {
        redirectUrl
        departmentId
        __typename
      }
      related {
        relatedKeyword
        otherRelated {
          keyword
          url
          product {
            id
            name
            price
            imageUrl
            rating
            countReview
            url
            priceStr
            __typename
          }
          __typename
        }
        __typename
      }
      suggestion {
        currentKeyword
        suggestion
        suggestionCount
        instead
        insteadCount
        query
        text
        __typename
      }
      products {
        id
        name
        ads {
          id
          productClickUrl
          productWishlistUrl
          productViewUrl
          __typename
        }
        badges {
          title
          imageUrl
          show
          __typename
        }
        category: departmentId
        categoryBreadcrumb
        categoryId
        categoryName
        countReview
        discountPercentage
        gaKey
        imageUrl
        labelGroups {
          position
          title
          type
          __typename
        }
        originalPrice
        price
        priceRange
        rating
        shop {
          id
          name
          url
          city
          isOfficial
          isPowerBadge
          __typename
        }
        url
        wishlist
        sourceEngine: source_engine
        __typename
      }
      __typename
    }
    __typename
  }
}

"""

# requestPayload = {
#     "operationName":"SearchProductQueryV4",
#     "variables":{
#         "params":"scheme=https&device=desktop&related=true&st=product&q={}&ob=23&page=1&variants=&shipping=&start=0&rows={}&user_id=&unique_id=d2426b563c16fd7b333dff580e431f86&safe_search=false&source=search".format(productQuery,nListing)
#     },
#     "query":"query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      __typename\n    }\n    data {\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        shop {\n          id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
# }


""" PDPInfoQuery Complete Parameter
  query PDPInfoQuery($shopDomain:String, $productKey:String) {
      getPDPInfo(productID:0,shopDomain:$shopDomain,productKey:$productKey) {
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
              detail{id
              name
              breadcrumbURL
          }
      }
      pictures{picID fileName filePath description isFromIG width height urlOriginal urlThumbnail url300 status}
      preorder{isActive duration timeUnit}
      wholesale{minQty price}
      videos{source url}
      campaign{campaignID campaignType campaignTypeName originalPrice discountedPrice isAppsOnly isActive percentageAmount stock originalStock startDate endDate endDateUnix appLinks hideGimmick}
      stats{countView countReview countTalk rating}
      txStats{txSuccess txReject itemSold itemSoldPaymentVerified}
      cashback{percentage}
      variant{parentID isVariant}
      stock{useStock value stockWording}
      menu{name}
      }
  }"
"""

""" PDPShopInfoQuery Complete Parameter
  "query PDPShopInfoQuery($fields:[String!]!,$domain:String) {
    shopInfo:shopInfoByID(input:{shopIDs:[0]) {
      result {
        favoriteData {
          alreadyFavorited
        }
        goldOS {
          isGold 
          isGoldBadge 
          isOfficial 
          badgeSVG 
          title
        }
        isAllowManage 
        shopLastActive 
        location 
        shippingLoc {
          districtName 
          cityName
        }
        shopAssets{avatar}
        shopCore{description domain shopID name url}
        statusInfo{shopStatus statusMessage statusTitle}
        closedInfo{closedNote until reason}}
        error{message}}}"
"""

shopID = ["7503026"]
shopDomain = "supergamingid"
productKey = 'intel-core-i5-10400f-coffee-lake-promo-gaming-murah'
productID = 846938257

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



# byUrlPayload = {
#     "operationName":"PDPInfoQuery",
#     "variables":{
#         "shopDomain" : shopDomain,
#         "productKey" : productKey
#     },
#     "query": "query PDPInfoQuery($shopDomain:String, $productKey:String){\n  getPDPInfo(productID:0,shopDomain:$shopDomain,productKey:$productKey) {\n  basic {id\n    shopID\n    name\n    alias\n    price\n    lastUpdatePrice\n    status\n    url} stats{\n countView\n countReview\n rating\n} txStats{\n txSuccess\n txReject\n itemSold\n itemSoldPaymentVerified\n} stock{\n useStock\n value\n stockWording\n}  }}"
# }

# byProductID = {
#     "operationName":"PDPInfoQuery",
#     "variables":{
#         "productID" : productID
#     },
#     "query": "query PDPInfoQuery($productID:Int){\n  getPDPInfo(productID:$productID) {\n  basic {id\n    shopID\n    name\n    alias\n    price\n    lastUpdatePrice\n    status\n    url} stats{\n countView\n countReview\n rating\n} txStats{\n txSuccess\n txReject\n itemSold\n itemSoldPaymentVerified\n} stock{\n useStock\n value\n stockWording\n}  }}"
# }


r = requests.post(url = API_ENDPOINT, json=shopInfoQuery)

dataTree = r.json()

print('')