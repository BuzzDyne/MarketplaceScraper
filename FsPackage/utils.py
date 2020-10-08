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

def cleanseTagInput(inputStr):
    # Filter Non-AlphaNumeric
    inputStr = re.sub('[^0-9a-zA-Z]+', " ", inputStr)
    # Remove trailing and leading spaces
    inputStr = inputStr.strip()
    # To Lower case
    inputStr = inputStr.lower()

    return inputStr