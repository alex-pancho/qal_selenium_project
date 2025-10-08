from pages.base_page import BasePage


class CartPage(BasePage):
        def __init__(self, driver):
                super().__init__(driver)
        
        proceed_to_checkout_button = "//a[@class='btn btn-default check_out']"
        add_comment_field = "//textarea[@class='form-control']"
        place_order_button = "//a[@class='btn btn-default check_out']"
        empty_cart_text = "//*[text()='Cart is empty!']"
