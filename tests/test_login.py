import pytest
from pages.login_page import LoginPage
    
def test_login_data_incorrect(login_page: LoginPage):
    login_page.enter_email("test@1secmail.com")
    login_page.enter_password("wrongpassword")
    login_page.click_login()
    assert login_page.is_error_message_presented()

def test_login_empty_fields(login_page: LoginPage):
    login_page.enter_email("")
    login_page.enter_password("")
    login_page.click_login()
    assert login_page.is_still_on_login_page()

def test_login_empty_password(login_page: LoginPage):
    login_page.enter_email("testtanya@test.com")
    login_page.enter_password("")
    login_page.click_login()
    assert login_page.is_still_on_login_page()

def test_login_empty_email(login_page: LoginPage):
    login_page.enter_email("")
    login_page.enter_password("test1234")
    login_page.click_login()
    assert login_page.is_still_on_login_page()

def test_login_valid_credentials(login_page: LoginPage):
    login_page.enter_email("testtanya123@test.com")
    login_page.enter_password("test1234")
    login_page.click_login()
    assert login_page.is_logout_button_presented()
