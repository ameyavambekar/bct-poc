import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class HomePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "//input[@class='search-field']"
    _search_button = "//button[@value='Search']"
    _products_list = "//ul[contains(@class,'products')]//li"

    def search_product(self, product_name):
        self.sendKeys(product_name, self._search_box, "xpath")
        self.clickElement(self._search_button, "xpath")

    def select_product_from_list(self, index):
        products = self.getElementList(self._products_list, "xpath")
        try:
            product = products[index-1]
            self.clickElement(element=product)
        except IndexError:
            self.log.error("There are only " + str(len(products)) + " displayed on page")


