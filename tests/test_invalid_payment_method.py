from pages.homepage import HomePage
from pages.productpage import ProductPage
from pages.cartpage import CartPage
from pages.checkoutpage import CheckoutPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class PlaceOrderTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.ts = TestStatus(self.driver)
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)
        self.cp = CartPage(self.driver)
        self.cop = CheckoutPage(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("D:\\python-workspace\\POC\\test_data.csv"))
    @unpack
    def test_invalidPaymentMethod(self, firstName, lastName, country, address, city, state, zip_code,
                                  phone, email):
        self.hp.select_product_from_list(1)
        self.pp.clickAddToCart()
        self.pp.clickViewCart()
        self.cp.clickCheckoutButton()
        self.cop.enterBillingDetailsAndPlaceOrder(firstName, lastName, country, address, city, state,
                                                  zip_code, phone, email)
        result = self.cop.verifyInvalidPaymentMethod()
        self.ts.markFinal("invalidPaymentMethod", result, "Payment method is invalid")
