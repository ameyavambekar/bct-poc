from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from selenium.webdriver.common.keys import Keys
import time


class CheckoutPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _first_name_textbox = "billing_first_name"
    _last_name_textbox = "billing_last_name"
    _country_dropdown = "//span[contains(@aria-labelledby,'billing_country')]"
    _country_textbox = "//input[contains(@aria-owns,'billing_country')]"
    _country_list = "//ul[@id='select2-billing_country-results']//li"
    _address_textbox = "billing_address_1"
    _city_textbox = "billing_city"
    _state_dropdown = "//span[contains(@aria-labelledby,'billing_state')]"
    _state_textbox = "//input[contains(@aria-owns,'billing_state')]"
    _zip_textbox = "billing_postcode"
    _phone_textbox = "billing_phone"
    _email_textbox = "billing_email"
    _invalid_payment_method = "//ul[@class='woocommerce-error']//li"
    _place_order_button = "place_order"

    def enterFirstName(self, firstName):
        self.sendKeys(firstName, self._first_name_textbox)

    def enterLastName(self, lastName):
        self.sendKeys(lastName, self._last_name_textbox)

    def selectCountry(self, country):
        self.clickElement(self._country_dropdown, "xpath")
        self.sendKeys(country, self._country_textbox, "xpath")
        countries = self.getElementList(self._country_list, "xpath")
        for country_in_list in countries:
            if self.getText(element=country_in_list).lower() == country.lower():
                self.clickElement(element=country_in_list)

    def enterAddress(self, address):
        self.sendKeys(address, self._address_textbox)

    def enterCity(self, city):
        self.sendKeys(city, self._city_textbox)

    def selectState(self, state):
        self.clickElement(self._state_dropdown, "xpath")
        self.sendKeys(state, self._state_textbox, "xpath")
        self.sendKeys(Keys.ENTER, self._state_textbox, "xpath")

    def enterZipCode(self, zip_code):
        self.sendKeys(zip_code, self._zip_textbox)

    def enterPhoneNumber(self, number):
        self.sendKeys(number, self._phone_textbox)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_textbox)

    def clickPlaceOrderButton(self):
        self.waitForElement(self._place_order_button)
        self.clickElement(self._place_order_button)

    def enterBillingDetailsAndPlaceOrder(self, firstName, lastName, country, address, city, state, zipcode,
                                         phone, email):
        self.enterFirstName(firstName)
        self.enterLastName(lastName)
        self.selectCountry(country)
        self.enterAddress(address)
        self.enterCity(city)
        self.selectState(state)
        self.enterZipCode(zipcode)
        self.enterPhoneNumber(number=phone)
        self.enterEmail(email)
        time.sleep(3)
        self.clickPlaceOrderButton()

    def verifyInvalidPaymentMethod(self):
        return self.isElementDisplayed(self._invalid_payment_method, "xpath")
