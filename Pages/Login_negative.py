from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage


class LoggedInUnsuccessfully(BasePage):

    _url = 'https://phptravels.org/login'
    __feedback_locator = (By.XPATH, '//*[@id="main-body"]/div/div[1]/div/form/div/div[1]/div[2]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def feedback(self) -> str:
        return self._get_text(self.__feedback_locator)
