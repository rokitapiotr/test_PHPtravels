import pytest
from lib.Login_page import LoginPage
from lib.Login_negative import LoggedInUnsuccessfully
from conftest import driver


class TestNegativeLoginScenario:

    @pytest.mark.account_log_in
    @pytest.mark.negative
    def test_negative_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login('testmail@gmai.com', 'NogaRekaPlecy12')
        login_page.captcha('6LdJtY8UAAAAADTgIWYnG_VKkfNqqB-w8CdQFL7Y', 'https://phptravels.org/login')
        negative_logging = LoggedInUnsuccessfully(driver)
        assert negative_logging.expected_url == negative_logging.current_url, "Actual URL is not the same as expected"
        assert negative_logging.feedback == 'Login Details Incorrect. Please try again.', "Feedback is not displayed"
