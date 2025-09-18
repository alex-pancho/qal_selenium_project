from base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    menu_home = '//a[text()="Home"]'
    sign_in_button = '//button[.="Sign In"]'
    contacts_head = '//h2'
    sign_up_button = '//button[.="Sign Up"]'
    username_by = '//[@name="email"]'
    password_by = '//*[@id="signinPassword"]'
    signin_by = '//form//div[.="Login"]'

if __name__ == "__main__":
    driver = ""
    my_home = HomePage(driver)
    item = my_home.item("menu_home")
    print(item)
