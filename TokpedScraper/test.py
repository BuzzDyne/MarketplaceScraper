import csv
import os
import time


# myUtil.writeToCSV("This is the best", 1591704845)

d = ScrapeDriver()

d.driver.close()

d.openUrl('https://www.tokopedia.com/search?st=product&q=Ayam',"//span[@class='css-1bjwylw']")


