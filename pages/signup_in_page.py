from pages.base_page import BasePage


class SignupPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    input_name = '//input[@data-qa="signup-name"]'
    input_email = '//input[@data-qa="signup-email"]'
    signup_button = '//button[@data-qa="signup-button"]'
    signup_page_text = '//*[text()="Enter Account Information"]'
    
    input_email_login = '//input[@data-qa="login-email"]'
    password = '//input[@data-qa="login-password"]'
    login_button = '//button[@data-qa="login-button"]'

    # error_message  = '//*[text()="Your email or password is incorrect!"]'
    # error_message = '//p[contains(text(), "Your email or password is incorrect")]'
    # error_message = '//form[@action="/login"]//p[contains(normalize-space(.), "Your email or password is incorrect!")]'
    error_message = "//div[@class='login-form']//p[text()='Your email or password is incorrect!']"
    
    img_src = '//img[@alt="Website for automation practice"]'
    home = '//a[text()=" Home"]'
    products = '//a[text()=" Products"]'
    cart = '//a[text()=" Cart"]'
    signup_login = '//a[normalize-space(text())="Signup / Login"]'
    test_cases = '//a[normalize-space(text())="Test Cases"]'
    api_testing = '//a[normalize-space(text())="API Testing"]'
    video_tutorials = '//a[normalize-space(text())="Video Tutorials"]'
    contact_us = '//a[normalize-space(text())="Contact us"]'

    subscription = '//h2[contains(text(),"Subscription")]'
    fuuter_text = '//p[text()="Get the most recent updates from "]'
    input_email = '//input[@id="susbscribe_email"]'
    