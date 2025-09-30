from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/abina/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe") #C:\Users\abina\Downloads\chromedriver-win64 (1)\chromedriver-win64
driver = webdriver.Chrome(service=service_obj)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.implicitly_wait(5)


driver.switch_to.frame("singleframe")

driver.find_element(By.XPATH,"(//input[@type='text'])[1]").send_keys("Abinasha")

# driver.switch_to.default_content()
#
# txt = driver.find_element(By.XPATH,"//h3").text
#
# assert txt == "An iFrame containing the TinyMCE WYSIWYG Editor"



driver.quit()