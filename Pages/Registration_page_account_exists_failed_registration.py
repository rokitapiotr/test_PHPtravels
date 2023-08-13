from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage


class RegisteredUnSuccessfulOnRegistrationPageAccountExists(BasePage):
    _url = 'https://phptravels.org/register.php'
    __header_locator = (By.XPATH, '//*[@id="main-body"]/div/div[1]/div[2]/div[1]/ul/li')
    __error_of_resending_email_message_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/span')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)
