import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe") #C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.maximize_window()
driver.implicitly_wait(5)


# driver.find_element(By.ID,"downloadButton").click()

#edit the excel with updated value
file_input = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file_path = "C:\\Users\\abina\\Downloads\\download.xlsx"
file_input.send_keys(file_path)


WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[text()='Updated Excel Data Successfully.']")))#css selector =".Toastify__toast-body div:nth-child(2)"
upload_text=driver.find_element(By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)").text
print(upload_text)
fruit_name = "Apple"
price_column=driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
actual_price = driver.find_element(By.XPATH,f"//div[text()='{fruit_name}']/parent::div/parent::div/div[@id='cell-{price_column}-undefined']/div").text
print("The Actual price of the apple is :",actual_price)

time.sleep(2)
driver.quit()