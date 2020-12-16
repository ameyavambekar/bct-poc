from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from re import sub


class ProductPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver = driver

    # locators
    _product_title = "//h1[contains(@class,'product_title')]"
    _product_price = "//p[@class='price']/span"
    _minus_quantity = "//a[@class='minus']"
    _plus_quantity = "//a[@class='plus']"
    _add_to_cart_button = "//button[@name='add-to-cart']"
    _view_cart_link = "//a[@title='View cart']"

    def clickAddToCart(self):
        self.clickElement(self._add_to_cart_button, 'xpath')

    def clickViewCart(self):
        self.waitForElement(self._view_cart_link, 'xpath')
        self.clickElement(self._view_cart_link, 'xpath')

    def verifyProductTitle(self, title_to_verify):
        return self.getText(self._product_title, 'xpath').lower() == title_to_verify.lower()

    def verifyProductPrice(self, price_to_verify):
        priceWithCurrency = self.getText(self._product_price, 'xpath')
        actualPrice = float(sub(r'[^\d.]', '', priceWithCurrency))
        return price_to_verify == actualPrice
