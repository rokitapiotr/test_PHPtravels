from selenium.webdriver.remote.webdriver import WebDriver
from Base_page import BasePage
from locators import RegisteredUnSuccessfulOnRegistrationPageAccountExistsLocators


class RegisteredInSuccessfullyOnRegistrationPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return RegisteredUnSuccessfulOnRegistrationPageAccountExistsLocators.url

    @property
    def header(self) -> str:
        return self.get_text(RegisteredUnSuccessfulOnRegistrationPageAccountExistsLocators.header_locator)

    @property
    def error_message(self) -> str:
        return self.get_text(RegisteredUnSuccessfulOnRegistrationPageAccountExistsLocators.
                              error_of_resending_email_message_locator)
