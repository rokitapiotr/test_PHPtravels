import pytest
from test_PHPtravels.Pages.Login_page import LoginPage
from test_PHPtravels.Pages.Login_positive import LoggedInSuccessfully


class TestPositiveLoginScenario:

    @pytest.mark.account_log_in
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login('testmail@gmai.com', 'NogaRekaPlecy1234')
        login_page.captcha('6LdJtY8UAAAAADTgIWYnG_VKkfNqqB-w8CdQFL7Y','https://phptravels.org/login')
        positive_logging = LoggedInSuccessfully(driver)
        assert positive_logging.expected_url == positive_logging.current_url, "Actual URL is not the same as expected"
        assert positive_logging.header == 'Client Area', "Header is not the same as expected"
        assert positive_logging.feedback == 'Logged in as:', "Feedback is not displayed"
        assert positive_logging.is_button_displayed, "Picture should be displayed"
