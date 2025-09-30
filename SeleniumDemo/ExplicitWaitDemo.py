import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
# product validation

expected_list=["Cucumber","Raspberry","Strawberry"]

products = driver.find_elements(By.XPATH,"//div[@class='product']//h4")

actual_list =[]
for product in products:
    p = product.text.split("-")
    name = p[0].strip()
    actual_list.append(name)
print(actual_list)
assert actual_list == expected_list

time.sleep(3)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count>0

for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#Sum Validation
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum +int(price.text)

print(sum)
total_amount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == total_amount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)


discounted_amount =float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)

print(discounted_amount)
assert total_amount > discounted_amount




time.sleep(3)

driver.quit()
