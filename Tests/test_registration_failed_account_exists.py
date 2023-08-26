import pytest

from test_PHPtravels.Pages.Registration_page import RegistrationPage
from test_PHPtravels.Pages.Registration_failed_account_exists import RegisteredUnSuccessfulOnRegistrationPageAccountExists


class TestNegativeScenarioAccountExists:

    @pytest.mark.registration
    @pytest.mark.negative
    def test_negative_login_account_exists(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open()
        registration_page.fill_all_personal_information('John', 'Doe', 'testmail@gmai.com', '123456789',
                                                        '+48')
        registration_page.fill_all_billing_address('Dupa', 'Makowa 6', 'Noga',
                                                   'Smolec', 'Dolnyslask', '55080', 'PL')
        registration_page.fill_additional_required_information('123456789')
        registration_page.password_generator('14')
        registration_page.not_accepting_email_newsletter()
        registration_page.captcha('6LdJtY8UAAAAADTgIWYnG_VKkfNqqB-w8CdQFL7Y', 'https://phptravels.org/register.php')
        fail_to_register_account_exists = RegisteredUnSuccessfulOnRegistrationPageAccountExists(driver)
        assert fail_to_register_account_exists.expected_url == fail_to_register_account_exists.current_url, "Actual URL is not the same as expected"
        assert fail_to_register_account_exists.header == 'A user already exists with that email address'
