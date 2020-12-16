from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from re import sub


class CartPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _checkout_button = "//a[contains(@class,'checkout-button')]"
    _cart_total = "//td[@data-title='Total']//strong/span"

    def clickCheckoutButton(self):
        self.clickElement(self._checkout_button,'xpath')

    def verifyCartTotal(self, expectedTotal):
        actualTotalWithCurrency = self.getText(self._cart_total, "xpath")
        actualTotal = float(sub(r"[^\d.]", "", actualTotalWithCurrency))
        return actualTotal == expectedTotal

