from pages.homepage import HomePage
from pages.productpage import ProductPage
from pages.navigationpage import NavigationBar
from ddt import ddt, data, unpack
from utilities.teststatus import TestStatus
from utilities.read_data import getCSVData
import unittest
import pytest


@ddt
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ProductSearchTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.ts = TestStatus(self.driver)
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)
        self.navigation = NavigationBar(self.driver)

    def setUp(self):
        self.navigation.clickHomeLink()

    @pytest.mark.run(order=1)
    @data(*getCSVData("D:\\python-workspace\\POC\\products.csv"))
    @unpack
    def test_valid_search_results(self, product, price):
        self.hp.search_product(product)
        result1 = self.pp.verifyProductTitle(product)
        result2 = self.pp.verifyProductPrice(price)
        self.ts.mark(result1, "Verify Title")
        self.ts.mark(result2, "Verify Price")
