import pytest
from lib.Login_page import LoginPage, LoggedInSuccessfully
from conftest import driver

test_data = [
    ('testmail@gmai.com', 'NogaRekaPlecy12')
]


class TestPositiveLoginScenario:

    @pytest.mark.account_log_in
    @pytest.mark.positive
    @pytest.mark.parametrize("email, password", test_data)
    def test_positive_login(self, driver, email, password):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(email, password)
        login_page.captcha('6LdJtY8UAAAAADTgIWYnG_VKkfNqqB-w8CdQFL7Y', 'https://phptravels.org/login')
        positive_logging = LoggedInSuccessfully(driver)

        assert positive_logging.expected_url == positive_logging.current_url, "Actual URL is not the same as expected"
        assert positive_logging.header == 'Client Area', "Header is not the same as expected"
        assert positive_logging.feedback == 'Logged in as:', "Feedback is not displayed"
        assert positive_logging.is_button_displayed, "Picture should be displayed"
