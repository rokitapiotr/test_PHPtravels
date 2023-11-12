import pytest
from lib.Login_page import LoginPage, LoggedInUnsuccessfully
from conftest import driver

test_data = [
    ('testmail@gmai.com', 'NogaRekaPlecy12')
]


class TestNegativeLoginScenario:

    @pytest.mark.account_log_in
    @pytest.mark.negative
    @pytest.mark.parametrize("email, password", test_data)
    def test_negative_login(self, driver, email, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(email, 'password')
        login_page.captcha('6LdJtY8UAAAAADTgIWYnG_VKkfNqqB-w8CdQFL7Y', 'https://phptravels.org/login')
        negative_logging = LoggedInUnsuccessfully(driver)

        assert negative_logging.expected_url == negative_logging.current_url, "Actual URL is not the same as expected"
        assert negative_logging.feedback == 'Login Details Incorrect. Please try again.', "Feedback is not displayed"
