from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Pages.Base_page import BasePage


class MainPage(BasePage):

    __url = "https://phptravels.com/"
    __demo_button = (By.XPATH, '//*[@id="content"]/section/div/div[1]/div/div[1]/a[1]')
    __first_name = (By.NAME, 'first_name')
    __last_name = (By.NAME, 'last_name')
    __business_name = (By.NAME, 'business_name')
    __email = (By.NAME, 'email')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_demonstration_version(self, first_name, last_name, business_name, email):
