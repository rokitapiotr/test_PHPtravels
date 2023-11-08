from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage


class RegistrationPage(BasePage):
    __url = "https://phptravels.org/register.php"
    __first_name = (By.ID, "inputFirstName")
    __last_name = (By.ID, "inputLastName")
    __email = (By.ID, "inputEmail")
    __phone_number = (By.ID, "inputPhone")
    __select_country_code = (By.XPATH, '//*[@id="containerNewUserSignup"]/div[1]/div/div/div[4]/div/div/div/div/div[2]')
    __company_name = (By.ID, 'inputCompanyName')
    __address_1 = (By.ID, 'inputAddress1')
    __address_2 = (By.ID, 'inputAddress2')
    __city = (By.ID, 'inputCity')
    __state = (By.ID, 'stateinput')
    __post_code = (By.ID, 'inputPostcode')
    __select_country = (By.XPATH, '//*[@id="inputCountry"]')
    __phone_number_2 = (By.ID, "customfield2")
    __password_generator_button = (By.XPATH, '//*[@id="containerPassword"]/div[4]/div/button')
    __password_length_input = (By.ID, 'inputGeneratePasswordLength')
    __generation_new_password_button = (
    By.XPATH, '//*[@id="modalGeneratePassword"]/div/div/div[2]/div[4]/div/button[1]')
    __copy_new_password_button = (By.XPATH, '//*[@id="modalGeneratePassword"]/div/div/div[2]/div[4]/div/button[2]')
    __copy_and_insert_password_button = (By.XPATH, '//*[@id="btnGeneratePasswordInsert"]')
    __newsletter_rejection = (By.XPATH, '//*[@id="frmCheckout"]/div[3]/div/div')
    __proving_that_i_am_not_a_robot_button = (By.XPATH, '//*[@id="recaptcha-anchor"]')
    __register_button = (By.XPATH, '//*[@id="frmCheckout"]/p/input')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._open_url(self.__url)

    def fill_all_personal_information(self,
                                      first_name: str,
                                      last_name: str,
                                      email: str,
                                      phone_number: str,
                                      country_code: str):
        self._type(self.__first_name, first_name)
        self._type(self.__last_name, last_name)
        self._type(self.__email, email)
        self._type(self.__phone_number, phone_number)
        self._select_div_by_value(self.__select_country_code, country_code)

    def fill_all_billing_address(self,
                                 company_name: str,
                                 street_address: str,
                                 street_address_2: str,
                                 city: str,
                                 state: str,
                                 post_code: str,
                                 country: str):
        self._type(self.__company_name, company_name)
        self._type(self.__address_1, street_address)
        self._type(self.__address_2, street_address_2)
        self._type(self.__city, city)
        self._type(self.__state, state)
        self._type(self.__post_code, post_code)
        self._select_by_value(self.__select_country, country)

    def fill_additional_required_information(self, phone_number: str):
        self._type(self.__phone_number_2, phone_number)

    def password_generator(self, length_of_password: str):
        self._click(self.__password_generator_button)
        self._type(self.__password_length_input, length_of_password)
        self._click(self.__generation_new_password_button)
        self._click(self.__copy_and_insert_password_button)

    def not_accepting_email_newsletter(self):
        self._click(self.__newsletter_rejection)

    def captcha(self, site_key: str, url_str: str):
        captcha_token = self._resolve_captcha(site_key, url_str)
        self._set_captcha_response(captcha_token)
        self._click(self.__register_button)
