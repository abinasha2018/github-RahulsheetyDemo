import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe") #C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)


driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()


product_card = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in product_card:
    product_name = product.find_element(By.XPATH,"//div/h4/a").text
    if product_name == "Samsung Note 8":
        product.find_element(By.XPATH,"//div/button").click()
        break
driver.find_element(By.CSS_SELECTOR,".nav-link.btn.btn-primary").click()

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

driver.find_element(By.ID,"country").send_keys("ind")

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

time.sleep(2)

driver.find_element(By.XPATH,"//label[@for='checkbox2']").click();

driver.find_element(By.XPATH,"//input[@value='Purchase']").click()

text_success_msg=driver.find_element(By.CSS_SELECTOR,".alert-dismissible").text

assert "Success! Thank you!" in text_success_msg


time.sleep(4)
driver.quit()