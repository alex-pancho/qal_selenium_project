import pytest

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver

from pages.home_page import HomePage
from pages.signup_in_page import SignupPage
from pages.cart_page import CartPage
from pages.item4_page import Item4_Page

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
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome() if debug else \
        webdriver.Chrome(options)
    return driver


@pytest.fixture(scope="module")
def driver():
    _driver = firefox(True)
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

@pytest.fixture
def item4_page(driver):
    driver.get(HomePage.URL + "/product_details/4")
    return Item4_Page(driver)
    
@pytest.fixture
def cart_page(driver):
    driver.get(HomePage.URL + "/view_cart")
    return CartPage(driver)