import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe") #C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


check_boxes = driver.find_elements(By.XPATH,"//div[@id='checkbox-example']//label/input")

for check_box in check_boxes:
    if check_box.get_attribute("value") == "option2":
        check_box.click()
        assert check_box.is_selected()
        break

time.sleep(2)
driver.quit()