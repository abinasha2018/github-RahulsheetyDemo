import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe") #C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")

time.sleep(2)

countrys = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")
print(len(countrys))

for country in countrys:
    if country.text == "India":
        country.click()
        break

# print(driver.find_element(By.ID,"autosuggest").text) This is not print the text in autosuggestion dropdown

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"


time.sleep(2)
driver.quit()

