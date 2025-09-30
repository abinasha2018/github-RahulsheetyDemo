import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe") #C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//a[contains(text(),'InterviewQues')]").click()

all_window_id=driver.window_handles

driver.switch_to.window(all_window_id[1])

text_of_chw=driver.find_element(By.XPATH,"//p[@class ='im-para red']").text

splitwords = text_of_chw.split(" ")
email = splitwords[4].strip()

print(email)

driver.close()

driver.switch_to.window(all_window_id[0])

driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password").send_keys("learning")

driver.find_element(By.CSS_SELECTOR,"#terms").click()

driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()

wait = WebDriverWait(driver, 10)
error_msg = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='alert alert-danger col-md-12']"))).text
print("Error message is:",error_msg)

# driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text




time.sleep(3)
driver.quit()