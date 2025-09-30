import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe") #C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(5)


driver.find_element(By.LINK_TEXT,"Click Here").click()
allWindowid = driver.window_handles

driver.switch_to.window(allWindowid[1])
childwindowtext = driver.find_element(By.TAG_NAME,"h3").text
print(childwindowtext)
assert childwindowtext == "New Window"

driver.close()

driver.switch_to.window(allWindowid[0])
ParentWindowText = driver.find_element(By.TAG_NAME,"h3").text

print(ParentWindowText)
assert ParentWindowText == "Opening a new window"

time.sleep(3)
driver.quit()
