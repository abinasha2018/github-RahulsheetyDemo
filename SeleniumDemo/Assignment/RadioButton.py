import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe") #C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radio_buttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
# radio_buttons = driver.find_elements(By.XPATH,"//label[contains(@for,'radio')]/input")

# for radio_button in radio_buttons:
#     if radio_button.get_attribute("value") == "radio3":
#         radio_button.click()
#         assert radio_button.is_selected()
#         break

radio_buttons[2].click()
assert radio_buttons[2].is_selected()

time.sleep(4)
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.XPATH,"//input[@id='hide-textbox']").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

time.sleep(2)
driver.quit()