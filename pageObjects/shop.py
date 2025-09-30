from selenium.webdriver.common.by import By

from pageObjects.checkout_confirmation import Checkout_Confirmation
from utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")

    def add_product_to_cart(self, excepted_product_name):

        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            product_name = product.find_element(By.XPATH, ".//div/h4/a").text
            if product_name == excepted_product_name :#"Samsung Note 8"
                product.find_element(By.XPATH, ".//div/button").click()
                break

    def go_to_cart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation

