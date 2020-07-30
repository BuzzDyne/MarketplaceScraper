import csv
import time
from re import sub

def filterNonNumericToInt(strX):
    return int(sub(r'[^0-9]', '', strX))

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
            w.writerow(["Timestamp","Listing Name","Listing Price","Sold","Seen","Review Score","Review Count","Store Name","Store Area","URL"])

            print("Created {}".format(fileName))
        else:
            print("{} exists, appending".format(fileName))

        for p in prodList:
            w.writerow(p.getData())