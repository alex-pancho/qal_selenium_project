import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def visible_product_titles(driver):
    """Вернуть список видимых (displayed) названий продуктов на странице."""
    elems = driver.find_elements(By.CSS_SELECTOR, ".productinfo p")
    titles = [e.text.strip() for e in elems if e.is_displayed() and e.text.strip()]
    return titles


@pytest.mark.usefixtures("driver")
def test_search_product(driver):
    driver.get("http://automationexercise.com")
    time.sleep(2)

    # Закрываем cookie-оверлей, если есть
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
    assert driver.current_url == expected_url, f"Очикували URL {expected_url}, получили {driver.current_url}"

    # Поиск "Top"
    search_input = driver.find_element(By.ID, "search_product")
    search_input.clear()
    search_input.send_keys("Top")

    search_button = driver.find_element(By.ID, "submit_search")
    search_button.click()

    # Дождаться, что появится секция Searched Products (поиск выполнен)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[text()='Searched Products']"))
    )
    time.sleep(1)

    titles = visible_product_titles(driver)
    assert len(titles) > 0, "Не найдены видимые продукты после поиска 'Top'"

    # Проверяем — есть хотя бы один видимый продукт, содержащий 'Top' (регистронезависимо)
    assert any("top" in t.lower() for t in titles), "Нет ни одного видимого продукта, содержащего 'Top'"


@pytest.mark.usefixtures("driver")
def test_search_no_results(driver):
    """Негативный тест: вводим 'Слон' и ожидаем отсутствие видимых совпадений."""
    driver.get("http://automationexercise.com")
    time.sleep(2)

    # Закрываем cookie-оверлей, если есть
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
    assert driver.current_url == expected_url, f"Очикували URL {expected_url}, получили {driver.current_url}"

    # Поиск "Слон"
    search_input = driver.find_element(By.ID, "search_product")
    search_input.clear()
    search_input.send_keys("Слон")

    search_button = driver.find_element(By.ID, "submit_search")
    search_button.click()

    # Дождаться секции результатов поиска (чтобы точно знать, что поиск отработал)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[text()='Searched Products']"))
    )
    time.sleep(1)

    titles = visible_product_titles(driver)

    # Утверждаем, что НЕТ видимых названий, содержащих "слон" (регистронезависимо)
    assert not any("слон" in t.lower() for t in titles), \
        f"Нашлись видимые продукты содержащие 'Слон' — { [t for t in titles if 'слон' in t.lower()] }"
