from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
        input_email_locator ="//input[@data-qa='login-email']"
        input_password_locator = "//input[@data-qa='login-password']"
        login_button_locator =  "//button[@data-qa='login-button']"
        error_message_locator = "//p[text()='Your email or password is incorrect!']"
        logout_button_locator = "//a[contains(text(), 'Logout')]"
        
    login_page_url = BasePage.URL + "/login"
    
    def enter_email(self, email):
        email_field = self.item.input_email_locator
        email_field.input_text(email)

    def enter_password(self, password):
        password_field = self.item.input_password_locator
        password_field.input_text(password)

    def click_login(self):
        self.item.login_button_locator.click()

    def is_error_message_presented(self):
        return self.item.error_message_locator.is_displayed()

    def is_still_on_login_page(self):
        return self.driver.current_url == self.login_page_url

    def is_logout_button_presented(self):
        return self.item.logout_button_locator.is_displayed()
    
