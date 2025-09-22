import pytest

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver

from pages.home_page import HomePage
from pages.signup_in_page import SignupPage

def firefox(debug=False):
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox() if debug else \
        webdriver.Firefox(options=options)
    driver.maximize_window()
    return driver


def chrome(debug=False):
    options = ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome() if debug else \
        webdriver.Chrome(options)
    return driver


@pytest.fixture(scope="module")
def driver():
    _driver = chrome(True)
    _driver.maximize_window()
    _driver.get(HomePage.URL)
    yield _driver
    _driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def signup_page(driver):
    driver.get(HomePage.URL + "/login")
    return SignupPage(driver)
