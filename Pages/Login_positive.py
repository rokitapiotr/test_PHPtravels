from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_PHPtravels.Pages.Base_page import BasePage


class LoggedInSuccessfully(BasePage):

    _url = 'https://phptravels.org/clientarea.php'
    __header_locator = (By.XPATH, '/html/body/nav/div/ol/li[2]')
    __logout_button_locator = (By.XPATH, '//*[@id="Secondary_Sidebar-Client_Shortcuts-Logout"]')
    __feedback_logged_as_locator = (By.XPATH, '//*[@id="header"]/div[1]/div/div/div[2]/div/div[1]/span')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)

    @property
    def feedback(self) -> str:
        return super()._get_text(self.__feedback_logged_as_locator)

    def is_button_displayed(self) -> bool:
        return super()._is_displayed(self.__logout_button_locator)