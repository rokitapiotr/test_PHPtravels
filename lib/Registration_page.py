from selenium.webdriver.remote.webdriver import WebDriver
from Base_page import BasePage
from locators import RegisteredSuccessfulOnRegistrationPageAccountExistsLocators
from locators import RegistrationPageLocators, RegisteredUnSuccessfulOnRegistrationPageAccountExistsLocators


class RegistrationPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self.open_url(RegistrationPageLocators.url)

    def fill_all_personal_information(self,
                                      first_name: str,
                                      last_name: str,
                                      email: str,
                                      phone_number: str,
                                      country_code: str):
        self.type(RegistrationPageLocators.first_name, first_name)
        self.type(RegistrationPageLocators.last_name, last_name)
        self.type(RegistrationPageLocators.email, email)
        self.type(RegistrationPageLocators.phone_number, phone_number)
        self.select_div_by_value(RegistrationPageLocators.select_country_code, country_code)

    def fill_all_billing_address(self,
                                 company_name: str,
                                 street_address: str,
                                 street_address_2: str,
                                 city: str,
                                 state: str,
                                 post_code: str,
                                 country: str):
        self.type(RegistrationPageLocators.company_name, company_name)
        self.type(RegistrationPageLocators.address_1, street_address)
        self.type(RegistrationPageLocators.address_2, street_address_2)
        self.type(RegistrationPageLocators.city, city)
        self.type(RegistrationPageLocators.state, state)
        self.type(RegistrationPageLocators.post_code, post_code)
        self.select_by_value(RegistrationPageLocators.select_country, country)

    def fill_additional_required_information(self, phone_number: str):
        self.type(RegistrationPageLocators.phone_number_2, phone_number)

    def password_generator(self, length_of_password: str):
        self.click(RegistrationPageLocators.password_generator_button)
        self.type(RegistrationPageLocators.password_length_input, length_of_password)
        self.click(RegistrationPageLocators.generation_new_password_button)
        self.click(RegistrationPageLocators.copy_and_insert_password_button)

    def not_accepting_email_newsletter(self):
        self.click(RegistrationPageLocators.newsletter_rejection)

    def captcha(self, site_key: str, url_str: str):
        captcha_token = self.resolve_captcha(site_key, url_str)
        self.set_captcha_response(captcha_token)
        self.click(RegistrationPageLocators.register_button)


class RegisteredUnsuccessfulOnRegistrationPageAccountExists(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return RegisteredUnSuccessfulOnRegistrationPageAccountExistsLocators.url

    @property
    def header(self) -> str:
        return self.get_text(RegisteredUnSuccessfulOnRegistrationPageAccountExistsLocators.header_locator)


class RegisteredInSuccessfullyOnRegistrationPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return RegisteredSuccessfulOnRegistrationPageAccountExistsLocators.url

    @property
    def header(self) -> str:
        return self.get_text(RegisteredSuccessfulOnRegistrationPageAccountExistsLocators.header_locator)

    @property
    def error_message(self) -> str:
        return self.get_text(RegisteredSuccessfulOnRegistrationPageAccountExistsLocators.
                             error_of_resending_email_message_locator)
