from selenium.webdriver.remote.webdriver import WebDriver
from Base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self.open_url(LoginPageLocators.url)

    def login(self, email, password):
        self.type(LoginPageLocators.email_input, email)
        self.type(LoginPageLocators.password_input, password)

    def captcha(self, site_key: str, url_str: str):
        captcha_token = self.resolve_captcha(site_key, url_str)
        self.set_captcha_response(captcha_token)
        self.click(LoginPageLocators.login_button)
