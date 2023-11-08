from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Pages.Base_page import BasePage


class DemoPage(BasePage):

    __url = "https://phptravels.com/demo"
    __demo_button = (By.ID, 'demo')
    __first_name = (By.NAME, 'first_name')
    __last_name = (By.NAME, 'last_name')
    __business_name = (By.NAME, 'business_name')
    __email = (By.NAME, 'email')
    __number1 = (By.XPATH, '//*[@id="numb1"]')
    __number2 = (By.XPATH, '//*[@id="numb2"]')
    __insert_number = (By.XPATH, '//*[@id="number"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._open_url(self.__url)

    def execute_demonstration_version(self, first_name, last_name, business_name, email):
        self._type(self.__first_name, first_name)
        self._type(self.__last_name, last_name)
        self._type(self.__business_name, business_name)
        self._type(self.__email, email)

        number1 = int(super()._get_text(self.__number1))
        number2 = int(super()._get_text(self.__number2))

        sum_of_numbers = number1 + number2

        self._type(self.__insert_number, str(sum_of_numbers))
        self._click(self.__demo_button)
