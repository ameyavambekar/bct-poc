import unittest
from tests.test_search_product import ProductSearchTest
from tests.test_invalid_payment_method import PlaceOrderTest

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(ProductSearchTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(PlaceOrderTest)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
