from base.basepage import BasePage


class NavigationBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _home_link = "//div[@class='main-navigation']//a[text()='Home']"
    _about_us_link = "//div[@class='main-navigation']//a[text()='About Us']"
    _products_link = "//div[@class='main-navigation']//a[text()='Products']"

    def clickHomeLink(self):
        self.clickElement(self._home_link, "xpath")

    def clickAboutUsLink(self):
        self.clickElement(self._about_us_link, "xpath")

    def clickProductsLink(self):
        self.clickElement(self._products_link, "xpath")
