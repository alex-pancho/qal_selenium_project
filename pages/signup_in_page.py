from pages.base_page import BasePage


class SignupPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    input_name = '//input[@data-qa="signup-name"]'
    input_email = '//input[@data-qa="signup-email"]'
    signup_button = '//button[@data-qa="signup-button"]'
    signup_page_text = '//*[text()="Enter Account Information"]'