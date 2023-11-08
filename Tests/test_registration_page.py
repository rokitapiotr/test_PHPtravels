import pytest

from Pages.Registration_page import RegistrationPage
from Pages.Registration_page_succesfull import RegisteredInSuccessfullyOnRegistrationPage


class TestPositiveScenariosForRegistrationPage:

    @pytest.mark.registration
    @pytest.mark.positive
    def test_successful_registration(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.open()
        registration_page.fill_all_personal_information('John', 'Doe', 'dupa112349807@onet.pl', '123456789',
                                                        '+48')
        registration_page.fill_all_billing_address('Dupa', 'Makowa 6', 'Fiut',
                                                   'Smolec', 'Dolnyslask', '55080', 'PL')
        registration_page.fill_additional_required_information('123456789')
        registration_page.password_generator('14')
        registration_page.not_accepting_email_newsletter()
        registration_page.captcha('6LdJtY8UAAAAADTgIWYnG_VKkfNqqB-w8CdQFL7Y', 'https://phptravels.org/register.php')
        logged_in_registration_page = RegisteredInSuccessfullyOnRegistrationPage(driver)
        assert logged_in_registration_page.expected_url == logged_in_registration_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_registration_page.error_message == 'Please check your email and follow the link to verify your email address.'
        assert logged_in_registration_page.header == 'Client Area'
