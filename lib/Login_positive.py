from selenium.webdriver.remote.webdriver import WebDriver
from Base_page import BasePage
from locators import LoggedInSuccessfullyLocators


class LoggedInSuccessfully(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return LoggedInSuccessfullyLocators.url

    @property
    def header(self) -> str:
        return self.get_text(LoggedInSuccessfullyLocators.header_locator)

    @property
    def feedback(self) -> str:
        return self.get_text(LoggedInSuccessfullyLocators.feedback_logged_as_locator)

    def is_button_displayed(self) -> bool:
        return self.is_displayed(LoggedInSuccessfullyLocators.logout_button_locator)
