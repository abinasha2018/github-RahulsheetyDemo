import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe") #C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()
#locators:-Id,Name,Xpath,Cssselector,Classname,linktext

driver.find_element(By.NAME,"email").send_keys("AbinashaDash@Gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("abc123")
driver.find_element(By.ID,"exampleCheck1").click()


#Xpath-----//tagname[@attribute name = "Av"]
#cssselector-----tagname[attribute name = "Av"]  (#id) (.classname)
# //there is a property called which is grab the text present in this element
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Abinasha")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

time.sleep(3)
#Satic Dropdown
Dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
Dropdown.select_by_visible_text("Female")
Dropdown.select_by_index(0)
# Dropdown.select_by_value("Male")

time.sleep(2)

driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

time.sleep(2)
# assert "Success! The Form has been submitted successfully!." in message ,"Failed"
assert "Success!" in message,"Failed"

driver.find_element(By.CSS_SELECTOR,".ng-untouched").clear()

time.sleep(2)
driver.quit()
