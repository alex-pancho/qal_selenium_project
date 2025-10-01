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
        self.logout_button_locator = (By.XPATH, "//a[contains(text(), 'Logout')]")
    
    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.input_email_locator)
        )
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.input_password_locator)
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.login_button_locator)
        ).click()

    def is_error_message_presented(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.error_message_locator)
            )
            return True
        except:
            return False

    def is_still_on_login_page(self):
        return self.driver.current_url == "https://automationexercise.com/login"
    
    def is_logout_button_presented(self):
        try:
            WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.logout_button_locator)
            )
            return True
        except:
            return False
