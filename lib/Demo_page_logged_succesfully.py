from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage


class LoggedInSuccessfullyOnDemoPage(BasePage):

    __header_locator = (By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/h2')
    __picture_locator = (By.XPATH, '//*[@id="colored"]')
    __feedback_locator = (By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/p')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def header(self) -> str:
        return self._get_text(self.__header_locator)

    @property
    def feedback(self) -> str:
        return self._get_text(self.__feedback_locator)

    def is_picture_displayed(self) -> bool:
        return self._is_displayed(self.__picture_locator)

