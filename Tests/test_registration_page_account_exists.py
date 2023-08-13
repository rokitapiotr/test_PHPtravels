import pytest

from Pages.Registration_page import RegistrationPage
from Pages.Registration_page_account_exists_failed_registration import \
    RegisteredUnSuccessfulOnRegistrationPageAccountExists


class TestNegativeScenarioAccountExists:

    @pytest.mark.account_log_in
    @pytest.mark.positive
    def test_negative_login_account_exists(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open()
        registration_page.fill_all_personal_information('John', 'Doe', 'dupa12347@onet.pl', '123456789',
                                                        '+48')
        registration_page.fill_all_billing_address('Dupa', 'Makowa 6', 'Fiut',
                                                   'Smolec', 'Dolnyslask', '55080', 'PL')
        registration_page.fill_additional_required_information('123456789')
        registration_page.password_generator('14')
        registration_page.not_accepting_email_newsletter()
        registration_page.captcha('6LdJtY8UAAAAADTgIWYnG_VKkfNqqB-w8CdQFL7Y')
        fail_to_register_account_exists = RegisteredUnSuccessfulOnRegistrationPageAccountExists(driver)
        assert fail_to_register_account_exists.expected_url == fail_to_register_account_exists.current_url, "Actual URL is not the same as expected"
        assert fail_to_register_account_exists.header == 'A user already exists with that email address'
