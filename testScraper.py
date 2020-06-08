from selenium import webdriver
import time

CHROME_PATH = "D:\chromedriver.exe"

driver = webdriver.Chrome(CHROME_PATH)

driver.get("https://www.google.com")

print(driver.title)

# Close Tab
driver.close() 

# Quit Browser
# driver.quit()