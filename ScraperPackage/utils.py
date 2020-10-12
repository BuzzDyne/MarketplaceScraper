import csv
import time
from re import sub

def filterNonNumericToInt(strX):
    """Takes STRING and returns only the number in the string as INTEGER"""
    return int(sub(r'[^0-9]', '', strX))

def shopAreaCleaner(dirtyStore):
    aktifNo = dirtyStore.find("Aktif")
    onlineNo= dirtyStore.find("Online")

    if(aktifNo == -1):
        output = dirtyStore[0:onlineNo-3]
    elif(onlineNo == -1):
        output = dirtyStore[0:aktifNo-3]
    else:
        output = "ShopAreaCleanerError"

    return output

def removeSpaceFileName(strX):
    return strX.replace(" ", "_")

def convTimeEpochToStr(timeX):
    # "%d-%b-%Y-%H%M%S"
    # "%H%M%S-%Y-%b-%d"
    return time.strftime("%d-%b-%Y-%H%M%S", time.localtime(timeX))

def writeToCSV(qName, prodList, qTime):
    fileName = "{}_{}.csv".format(removeSpaceFileName(qName), convTimeEpochToStr(qTime))

    with open(fileName, 'a', newline='') as f:
        w = csv.writer(f)

        # Write Header
        if f.tell() == 0:
            w.writerow(["Timestamp", "Listing ID","Listing Name","Listing Price","Stock","Sold","Seen","Review Score","Review Count","Store Name","Store Area","URL"])

            print("Created {}".format(fileName))
        else:
            print("{} exists, appending".format(fileName))

        for p in prodList:
            w.writerow(p.getData())
