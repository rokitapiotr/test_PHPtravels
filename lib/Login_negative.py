from selenium.webdriver.remote.webdriver import WebDriver
from Base_page import BasePage
from locators import LoggedInUnsuccessfullyLocators


class LoggedInUnsuccessfully(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return LoggedInUnsuccessfullyLocators.url

    @property
    def feedback(self) -> str:
        return self.get_text(LoggedInUnsuccessfullyLocators.feedback_locator)
