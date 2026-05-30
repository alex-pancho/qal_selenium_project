import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def visible_product_titles(driver):
    """Повернути список видимих назв на сторінці"""
    elems = driver.find_elements(By.CSS_SELECTOR, ".productinfo p")
    titles = [e.text.strip() for e in elems if e.is_displayed() and e.text.strip()]
    return titles


@pytest.mark.usefixtures("driver")
def test_search_product(driver):
    driver.get("http://automationexercise.com")
    time.sleep(2)

    # Закриваєм cookie-оверлей, якщо є
    try:
        agree_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//p[text()="Соглашаюсь"]'))
        )
        agree_button.click()
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element((By.CLASS_NAME, "fc-dialog-overlay"))
        )
    except:
        pass

    # Перейти в Products
    products_button = driver.find_element(By.XPATH, '//a[text()=" Products"]')
    products_button.click()
    time.sleep(2)

    expected_url = "https://automationexercise.com/products"
    assert driver.current_url == expected_url, f"Очікували URL {expected_url}, получили {driver.current_url}"

    # Пошук по слову "Top"
    search_input = driver.find_element(By.ID, "search_product")
    search_input.clear()
    search_input.send_keys("Top")

    search_button = driver.find_element(By.ID, "submit_search")
    search_button.click()

    # Дочекатися що з'явиться Searched Products
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[text()='Searched Products']"))
    )
    time.sleep(1)

    titles = visible_product_titles(driver)
    assert len(titles) > 0, "Не найдені продукти після пощуку 'Top'"

    # Перевіряємо що є хоча б один продукт 'Top'
    assert any("top" in t.lower() for t in titles), "Немає жодного продукту  'Top'"


@pytest.mark.usefixtures("driver")
def test_search_no_results(driver):
    """Негативний тест: вводим 'Слон' и очикуємо відсутність збігів."""
    driver.get("http://automationexercise.com")
    time.sleep(2)

    # Закриваємо cookie-оверлей, якщо є
    try:
        agree_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//p[text()="Соглашаюсь"]'))
        )
        agree_button.click()
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element((By.CLASS_NAME, "fc-dialog-overlay"))
        )
    except:
        pass

    # Перейти в Products
    products_button = driver.find_element(By.XPATH, '//a[text()=" Products"]')
    products_button.click()
    time.sleep(2)

    expected_url = "https://automationexercise.com/products"
    assert driver.current_url == expected_url, f"Очікували URL {expected_url}, получили {driver.current_url}"

    # Пошук по слову "Слон"
    search_input = driver.find_element(By.ID, "search_product")
    search_input.clear()
    search_input.send_keys("Слон")

    search_button = driver.find_element(By.ID, "submit_search")
    search_button.click()

    # Дочекатись секціі результатов пошуку (пошук відпрацював)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[text()='Searched Products']"))
    )
    time.sleep(1)

    titles = visible_product_titles(driver)

    # Намає продуктів "слон"
    assert not any("слон" in t.lower() for t in titles), \
        f"Найдені продукти що содержать 'Слон' — { [t for t in titles if 'слон' in t.lower()] }"
