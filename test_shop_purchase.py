import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestShopPurchase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=FirefoxService())
        self.driver.implicitly_wait(10)

    def test_shop_purchase_total(self):
        # Шаг 1: Открыть сайт магазина
        self.driver.get("https://www.saucedemo.com/")

        # Шаг 2: Авторизация
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user") \
                   .enter_password("secret_sauce") \
                   .click_login()

        # Шаг 3: Добавление товаров в корзину
        inventory_page = InventoryPage(self.driver)
        inventory_page.add_backpack() \
                     .add_tshirt() \
                     .add_onesie()

        # Шаг 4: Переход в корзину
        inventory_page.go_to_cart()

        # Шаг 5: Нажатие Checkout
        cart_page = CartPage(self.driver)
        cart_page.click_checkout()

        # Шаг 6: Заполнение формы
        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_personal_info("Иван", "Петров", "123456") \
                    .click_continue()

        # Шаг 7: Чтение итоговой стоимости
        total_amount = checkout_page.get_total_amount()

        # Шаг 8: Проверка итоговой суммы
        expected_total = "58.29"
        self.assertEqual(total_amount, expected_total,
                         f"Ожидаемая сумма: ${expected_total}, Фактическая сумма: ${total_amount}")

        print(f"Тест пройден успешно! Итоговая сумма: ${total_amount}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "main":
    unittest.main()