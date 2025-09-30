#in selenium package webdriver is a class name in selenium
#chrome is method if you calling chrome browser will open
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chrome driver service (it is a middleman interprets all webdriver commands)
service_obj = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe") #C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
driver = webdriver.Chrome(service=service_obj)
#driver is responsible to automate on chrome browser all webdriver methods we will be able to access from this driver objects which is object of this chrome class
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()

print(driver.title)

print(driver.current_url)





# driver = webdriver.Chrome() #one step to invoke browser
#
# driver.get("https://rahulshettyacademy.com")

#time is one class in python library
time.sleep(2)