from selenium.webdriver.remote.webdriver import WebDriver
from Base_page import BasePage
from locators import DemoPageLocators


class DemoPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self.open_url(DemoPageLocators.url)

    def execute_demonstration_version(self, first_name, last_name, business_name, email):
        self.type(DemoPageLocators.first_name, first_name)
        self.type(DemoPageLocators.last_name, last_name)
        self.type(DemoPageLocators.business_name, business_name)
        self.type(DemoPageLocators.email, email)

        number1 = int(self.get_text(DemoPageLocators.number1))
        number2 = int(self.get_text(DemoPageLocators.number2))

        sum_of_numbers = number1 + number2

        self.type(DemoPageLocators.insert_number, str(sum_of_numbers))
        self.click(DemoPageLocators.demo_button)
