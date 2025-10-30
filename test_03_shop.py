from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService


def test_shop_purchase_total():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox(service=FirefoxService())

    try:
        # Шаг 1: Открыть сайт магазина
        driver.get("https://www.saucedemo.com/")

        # Шаг 2: Авторизация
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Шаг 3: Добавление товаров в корзину
        # Ждем загрузки страницы с товарами
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
        )

        # Добавляем Sauce Labs Backpack
        backpack_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        backpack_add_button.click()

        # Добавляем Sauce Labs Bolt T-Shirt
        tshirt_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        tshirt_add_button.click()

        # Добавляем Sauce Labs Onesie
        onesie_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        onesie_add_button.click()

        # Шаг 4: Переход в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # Шаг 5: Нажатие Checkout
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        # Шаг 6: Заполнение формы
        first_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys("Иван")

        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Петров")

        postal_code_field = driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys("123456")

        # Шаг 7: Нажатие Continue
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        # Шаг 8: Чтение итоговой стоимости
        total_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text

        # Извлекаем числовое значение из текста
        total_amount = total_text.split("$")[1]

        # Шаг 9: Проверка итоговой суммы
        assert total_amount == "58.29", f"Ожидаемая сумма: $58.29, Фактическая сумма: ${total_amount}"

        print(f"Тест пройден успешно! Итоговая сумма: ${total_amount}")

    finally:
        # Закрытие браузера
        driver.quit()

if __name__ == "main":
    test_shop_purchase_total()