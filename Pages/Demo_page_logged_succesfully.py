from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage

class LoggedInSuccessfullyOnDemoPage(BasePage):

    __header_locator = (By.XPATH, '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/h2')
    __circle_locator = (By.XPATH, '//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div')
    __feedback_locator = (By.XPATH,'//*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/p')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)

    @property
    def feedback(self) -> str:
        return super()._get_text(self.__feedback_locator)

    def is_circle_displayed(self) -> bool:
        return super()._is_displayed(self.__circle_locator)

### //*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/h2/strong - Thank you!
### //*[@id="colored"] if element is disabled positive icon
### //*[@id="content"]/section[1]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/p - We have sent your demo credentials to your email please check your email to test demo website. if message not found inbox please check spam folder text