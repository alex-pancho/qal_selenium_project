
from selenium.webdriver.common.by import By

def test_add_item_to_cart(home_page):
    home_page.driver.execute_script("window.scrollTo(8, document.body.scrollHeight);")
    home_page.driver.execute_script("window.scrollTo(1000, 800);")
    last_height = home_page.driver.execute_script("return document.body.scrollHeight")
    button = home_page.item.element_stylish_dress_item
    button.click()
    
def test_item_view(item4_page):
    add_to_cart = item4_page.item.add_to_cart_button
    add_to_cart.click()
    added_item_text = item4_page.item.item_added_to_cart_popup 
    view_cart = item4_page.item.view_cart_button_popup
    view_cart.click()
    assert added_item_text.is_presented() == True


def test_check_item_in_cart(cart_page):
    cart_empty = cart_page.item.empty_cart_text
    proceed_button = cart_page.item.proceed_to_checkout_button
    proceed_button.click()
    # assert cart_empty.is_presented == False
  

