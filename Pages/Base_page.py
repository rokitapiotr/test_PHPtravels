import os
import sys
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from twocaptcha import TwoCaptcha


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 15):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _clear(self, locator: tuple, time: int = 15):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).clear()

    def _click(self, locator: tuple, time: int = 15):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 15):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 15):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def _select_by_value(self, locator: tuple, value: str, time: int = 15):
        self._wait_until_element_is_visible(locator, time)
        select = Select(self._find(locator))
        select.select_by_value(value)

    def _select_div_by_value(self, locator: tuple, country_code: str, time: int = 15):
        self._wait_until_element_is_visible(locator, time)
        div_element = self._find(locator)
        div_element.click()

        script = f"""
        var divElement = arguments[0];
        divElement.textContent = '{country_code}';
        """
        self._driver.execute_script(script, div_element)
        div_element.click()

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 15) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _resolve_captcha(self, site_key: str, url_str: str) -> str:
        sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

        api_key = os.getenv('1abc234de56fab7c89012d34e56fa7b8', 'dcb4b8fe00b2e43f5e02b2b19b3fbdbb')

        solver = TwoCaptcha(api_key)

        try:
            result = solver.recaptcha(
                sitekey=site_key,
                url=url_str
            )
            return str(result['code'])
        except Exception as e:
            return str(e)

    def _set_captcha_response(self, captcha_token):
        script = f'''
            var textarea = document.querySelector('textarea.g-recaptcha-response');
            textarea.style.display = 'block';
            textarea.value = '{captcha_token}';
        '''
        self._driver.execute_script(script)
