from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from test_PHPtravels.Pages.Base_page import BasePage


class LoginPage(BasePage):

    _url = 'https://phptravels.org/login'
    __email_input = (By.XPATH, '//*[@id="inputEmail"]')
    __password_input = (By.XPATH,'//*[@id="inputPassword"]')
    __login_button = (By.XPATH,'//*[@id="login"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._open_url(self._url)

    def login(self, email, password):
        self._type(self.__email_input, email)
        self._type(self.__password_input, password)

    def captcha(self, site_key: str, url_str: str):
        captcha_token = self._resolve_captcha(site_key, url_str)
        self._set_captcha_response(captcha_token)
        self._click(self.__login_button)
