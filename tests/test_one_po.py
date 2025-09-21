
def test_homepage_menu(home_page):
    element = home_page.item.menu_home
    assert element.is_visible(), f"Not found: {element._locator}"
    element.highlight_and_make_screenshot("menu_home.png")
