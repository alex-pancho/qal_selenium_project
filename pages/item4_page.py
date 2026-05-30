from pages.base_page import BasePage

    
class Item4_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    add_to_cart_button = "//button[@class='btn btn-default cart']"
    item_added_to_cart_popup = '//*[@class="modal-title w-100" and text()="Added!"]'
    view_cart_button_popup = '//a[@href="/view_cart"]'
if __name__ == "__main__":
    driver = ""
    my_home = Item4_Page(driver)
    item = my_home.item.menu_home
    print(item)