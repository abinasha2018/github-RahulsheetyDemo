from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_sort(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()
    driver.implicitly_wait(5)

    #Click on column header
    driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

    #collect all vaggie name -> BrowsersortedveggieList
    browser_sorted_veggies=[]
    vaggie_webelements = driver.find_elements(By.XPATH,"//tr/td[1]")
    for ele in vaggie_webelements:
        browser_sorted_veggies.append(ele.text)

    orginalbrowsersortedlist = browser_sorted_veggies.copy()
    print(orginalbrowsersortedlist)
    #Sort this veggielist => newSortedList
    browser_sorted_veggies.sort()
    print(browser_sorted_veggies)

    #BrowsersortedveggieList == newSortedList
    assert browser_sorted_veggies == orginalbrowsersortedlist




    driver.quit()


