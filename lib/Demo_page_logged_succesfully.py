from selenium.webdriver.remote.webdriver import WebDriver
from Base_page import BasePage
from locators import DemoPageLoggedSuccessfullyLocators


class LoggedInSuccessfullyOnDemoPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def header(self) -> str:
        return self.get_text(DemoPageLoggedSuccessfullyLocators.header_locator)

    @property
    def feedback(self) -> str:
        return self.get_text(DemoPageLoggedSuccessfullyLocators.feedback_locator)

    def is_picture_displayed(self) -> bool:
        return self.is_displayed(DemoPageLoggedSuccessfullyLocators.picture_locator)
