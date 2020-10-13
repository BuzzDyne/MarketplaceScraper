import re

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
