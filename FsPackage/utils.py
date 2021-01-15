import re
import requests

def tagifyListingName(inputStr):
    """
        Returns a list of search-tags formed from a given search string

        Example:
        Input = 'A B C'

        Output= ['A B C', 'A B', 'A C', 'B C', 'A', 'B', 'C']"""

    inputStr = cleanseTagInput(inputStr)

    tokenizedInput = inputStr.split()
    length = len(tokenizedInput)

    if(length <= 2):
        return tokenizedInput
    else:
        resTag = [inputStr]

        x = 0
        while(x != length-1):
            y = x + 1
            while (y < length):
                resTag.append("{} {}".format(tokenizedInput[x], tokenizedInput[y]))
                y = y +1
            x = x + 1

        resTag.extend(tokenizedInput)

        return resTag

def tagifyListingNameV2(inputStr):
    """
        Returns a list of search-tags formed from a given search string

        Example:
        Input = 'A B C D E F'

        Output= [
            'A B C D E F',
            'A B C D E',
            'B C D E F',
            'A B C D',
            'B C D E',
            'C D E F',
            'A B C',
            'B C D',
            'C D E',
            'D E F',
            'A B',
            'B C',
            'C D',
            'D E',
            'E F',
            'A', 'B', 'C', 'D', 'E', 'F'
        ]
    """

    inputStr = cleanseTagInput(inputStr)

    tokenizedInput = inputStr.split()
    length = len(tokenizedInput)
    takeLen = length

    resArr = []

    while(takeLen >= 1):
        startIndex = 1

        while(startIndex + takeLen <= length+1):
            kywd = sliceArr(tokenizedInput, startIndex, takeLen)
            resArr.append(' '.join(kywd))

            startIndex += 1

        takeLen -= 1
    
    return resArr

def cleanseTagInput(inputStr):
    # Filter Non-AlphaNumeric
    inputStr = re.sub('[^0-9a-zA-Z]+', " ", inputStr)
    # Remove trailing and leading spaces
    inputStr = inputStr.strip()
    # To Lower case
    inputStr = inputStr.lower()

    return inputStr

def sliceArr(arr, startIndex, length):
    if(startIndex < 1):
        print("sliceArr: startIndex Below One")
        return None

    if(length > len(arr)):
        print("sliceArr: Length over arrLength")
        return None

    newlist = arr[startIndex-1:]

    return newlist[:length]

def resolveShortUrl(url):
    """Will return the actual (long) url of a given url, whether short or long
    
    will return None if given link is not from tokopedia"""

    header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
    
    if("tokopedia.link" in url):
        r = requests.get(url, headers=header)
        url = r.url
        return url.split('?')[0]
    elif("tokopedia.com" in url):
        return url.split('?')[0]
    else:
        return None