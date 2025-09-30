from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe") #C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
driver = webdriver.Chrome(service=service_obj,options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print(driver.title)

driver.quit()