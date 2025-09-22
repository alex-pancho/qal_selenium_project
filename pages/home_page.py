from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    menu_home = '//ul[@class="nav navbar-nav"]'
    contacts_head = '//h2'
    sign_in_button = '//button[.="Sign In"]'
    sign_up_button = '//button[.="Sign Up"]'
    username_by = '//[@name="email"]'
    password_by = '//*[@id="signinPassword"]'
    signin_by = '//form//div[.="Login"]'
    contact_us = '//i[@class="fa")]'
    category_menu = '//div[@class="panel-group category-products"]'
    brands_menu = '//ul[@class="nav nav-pills nav-stacked")]'
    view_product = '//ul[@class="nav nav-pills nav-justified")]'
    features_items_section = '//div[@class="features_items"]'
    add_to_cart_feature_item = '(//div[@class="overlay-content"])[5]'
    view_cart = '//u[text()="View Cart"]'
    continue_shopping = '//button[text()="Continue Shopping"]'
    recommended_items_section = '//div[@class="recommended_items"]'
    add_to_cart_recommended_item = '//div[@class="carousel-inner"]//a[text()="Add to cart"]'
    subscription = '//input[@id="susbscribe_email"]'
    submit_subscribe = '//button[@id="subscribe"]'
    copyright = '//*[text()="Copyright ©"]'

if __name__ == "__main__":
    driver = ""
    my_home = HomePage(driver)
    item = my_home.item.menu_home
    print(item)
