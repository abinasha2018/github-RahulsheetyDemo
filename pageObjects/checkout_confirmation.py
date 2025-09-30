from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.browserutils import BrowserUtils


class Checkout_Confirmation(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, "//label[@for='checkbox2']")
        self.submit_button = (By.XPATH, "//input[@value='Purchase']")
        self.success_message = (By.CSS_SELECTOR, ".alert-dismissible")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self,countryName):

        self.driver.find_element(*self.country_input).send_keys(countryName)

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((self.country_option)))
        self.driver.find_element(*self.country_option).click()

        self.driver.find_element(*self.checkbox).click();
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        success_Text = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in success_Text


