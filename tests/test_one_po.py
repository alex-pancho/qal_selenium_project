
def test_homepage_menu(home_page):
    element = home_page.item.menu_home
    assert element.is_visible(), f"Not found: {element._locator}"


def test_sign_it_draft(signup_page):
    usename_field = signup_page.item.input_name
    email_field = signup_page.item.input_email
    button = signup_page.item.signup_button
    usename_field.send_keys("testuser")
    email_field.send_keys("testuser@1secmail.com")
    button.click()
    signup_text = signup_page.item.signup_page_text
    assert signup_text.get_text() == "ENTER ACCOUNT INFORMATION"