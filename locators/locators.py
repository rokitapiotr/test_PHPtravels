from selenium.webdriver.common.by import By


class DemonPageLocators:
    __url = "https://phptravels.com/demo"
    __demo_button = (By.ID, 'demo')
    __first_name = (By.NAME, 'first_name')
    __last_name = (By.NAME, 'last_name')
    __business_name = (By.NAME, 'business_name')
    __email = (By.NAME, 'email')
    __number1 = (By.XPATH, '//*[@id="numb1"]')
    __number2 = (By.XPATH, '//*[@id="numb2"]')
    __insert_number = (By.XPATH, '//*[@id="number"]')


class DemonPageLoggedSuccessfullyLocators:

    __header_locator = (By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/h2')
    __picture_locator = (By.XPATH, '//*[@id="colored"]')
    __feedback_locator = (By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/p')
