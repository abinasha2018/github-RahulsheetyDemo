#browser alert,Javascript alert
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name ="Abinasha"
service_obj = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe") #C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)

time.sleep(2)

# driver.find_element(By.ID,"alertbtn").click()
# alert = driver.switch_to.alert
# alert_text = alert.text
# assert name in alert_text
# alert.accept()

driver.find_element(By.ID,"confirmbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
assert name in alert_text
# alert.accept()
time.sleep(2)
alert.dismiss()

time.sleep(2)
driver.quit()
