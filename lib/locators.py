from selenium.webdriver.common.by import By


class DemoPageLocators:

    url = "https://phptravels.com/demo"
    demo_button = (By.ID, 'demo')
    first_name = (By.NAME, 'first_name')
    last_name = (By.NAME, 'last_name')
    business_name = (By.NAME, 'business_name')
    email = (By.NAME, 'email')
    number1 = (By.XPATH, '//*[@id="numb1"]')
    number2 = (By.XPATH, '//*[@id="numb2"]')
    insert_number = (By.XPATH, '//*[@id="number"]')


class DemoPageLoggedSuccessfullyLocators:

    header_locator = (By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/h2')
    picture_locator = (By.XPATH, '//*[@id="colored"]')
    feedback_locator = (By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/p')


class LoggedInUnsuccessfullyLocators:

    url = 'https://phptravels.org/login'
    feedback_locator = (By.XPATH, '//*[@id="main-body"]/div/div[1]/div/form/div/div[1]/div[2]')


class LoginPageLocators:

    url = 'https://phptravels.org/login'
    email_input = (By.XPATH, '//*[@id="inputEmail"]')
    password_input = (By.XPATH, '//*[@id="inputPassword"]')
    login_button = (By.XPATH, '//*[@id="login"]')


class LoggedInSuccessfullyLocators:

    url = 'https://phptravels.org/clientarea.php'
    header_locator = (By.XPATH, '/html/body/nav/div/ol/li[2]')
    logout_button_locator = (By.XPATH, '//*[@id="Secondary_Sidebar-Client_Shortcuts-Logout"]')
    feedback_logged_as_locator = (By.XPATH, '//*[@id="header"]/div[1]/div/div/div[2]/div/div[1]/span')


class RegistrationPageLocators:

    url = "https://phptravels.org/register.php"
    first_name = (By.ID, "inputFirstName")
    last_name = (By.ID, "inputLastName")
    email = (By.ID, "inputEmail")
    phone_number = (By.ID, "inputPhone")
    select_country_code = (By.XPATH, '//*[@id="containerNewUserSignup"]/div[1]/div/div/div[4]/div/div/div/div/div[2]')
    company_name = (By.ID, 'inputCompanyName')
    address_1 = (By.ID, 'inputAddress1')
    address_2 = (By.ID, 'inputAddress2')
    city = (By.ID, 'inputCity')
    state = (By.ID, 'stateinput')
    post_code = (By.ID, 'inputPostcode')
    select_country = (By.XPATH, '//*[@id="inputCountry"]')
    phone_number_2 = (By.ID, "customfield2")
    password_generator_button = (By.XPATH, '//*[@id="containerPassword"]/div[4]/div/button')
    password_length_input = (By.ID, 'inputGeneratePasswordLength')
    generation_new_password_button = (
        By.XPATH, '//*[@id="modalGeneratePassword"]/div/div/div[2]/div[4]/div/button[1]')
    copy_new_password_button = (By.XPATH, '//*[@id="modalGeneratePassword"]/div/div/div[2]/div[4]/div/button[2]')
    copy_and_insert_password_button = (By.XPATH, '//*[@id="btnGeneratePasswordInsert"]')
    newsletter_rejection = (By.XPATH, '//*[@id="frmCheckout"]/div[3]/div/div')
    proving_that_i_am_not_a_robot_button = (By.XPATH, '//*[@id="recaptcha-anchor"]')
    register_button = (By.XPATH, '//*[@id="frmCheckout"]/p/input')


class RegisteredSuccessfulOnRegistrationPageAccountExistsLocators:

    url = 'https://phptravels.org/clientarea.php'
    header_locator = (By.XPATH, '/html/body/nav/div/ol/li[2]')
    error_of_resending_email_message_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/span')


class RegisteredUnSuccessfulOnRegistrationPageAccountExistsLocators:

    url = 'https://phptravels.org/register.php'
    header_locator = (By.XPATH, '//*[@id="main-body"]/div/div[1]/div[2]/div[1]/ul/li')
    error_of_resending_email_message_locator = (By.XPATH, '/html/body/div[1]/div/div/div[2]/span')
