import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.safari.service import Service as Safari


@pytest.fixture(params=["chrome", "firefox", "safari"])
def driver(request):

    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver")

    match browser:
        case "chrome":
            my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        case "firefox":
            my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        case "safari":
            my_driver = webdriver.Safari(service=Safari(GeckoDriverManager().install()))
        case _:
            raise TypeError(f"Expected 'chrome', 'firefox' , 'safari', but got {browser}")

    my_driver.implicitly_wait(15)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome,firefox and Safari)"
    )
