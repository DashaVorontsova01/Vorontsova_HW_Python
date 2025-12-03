"""
Модуль содержит тесты для проверки процесса покупки в интернет-магазине.
Использует фреймворк unittest и библиотеку Allure для отчетности.
"""

import sys
import os
import unittest
import allure

# Добавляем родительскую директорию в путь для импорта модулей pages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestShopPurchase(unittest.TestCase):
    """
    Класс тестов для проверки полного цикла покупки в магазине.

    Наследуется от unittest.TestCase, содержит setup/teardown методы
    и тестовые методы.
    """

    def setUp(self) -> None:
        """
        Настройка перед каждым тестом.

        Инициализирует драйвер браузера Firefox и устанавливает
        неявное ожидание для элементов.

        Параметры:
            Нет
        Возвращает:
            None
        """
        self.driver = webdriver.Firefox(service=FirefoxService())
        self.driver.implicitly_wait(10)

    @allure.title("Проверка итоговой суммы покупки")
    @allure.description("Тест проверяет полный процесс покупки: "
                        "авторизацию, добавление товаров, оформление заказа "
                        "и сверку итоговой суммы")
    @allure.feature("Оформление заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shop_purchase_total(self) -> None:
        """
        Тест проверяет корректность расчета итоговой суммы покупки.

        Выполняет последовательность шагов:
        1. Открытие сайта
        2. Авторизация
        3. Добавление товаров в корзину
        4. Переход в корзину и оформление заказа
        5. Проверка итоговой суммы

        Параметры:
            Нет
        Возвращает:
            None
        """

        @allure.step("Открыть сайт магазина")
        def open_site() -> None:
            """Открывает главную страницу магазина."""
            self.driver.get("https://www.saucedemo.com/")

        @allure.step("Авторизация пользователя")
        def login() -> None:
            """Выполняет авторизацию с учетными данными стандартного пользователя."""
            login_page = LoginPage(self.driver)
            login_page.enter_username("standard_user") \
                .enter_password("secret_sauce") \
                .click_login()

        @allure.step("Добавление товаров в корзину")
        def add_products() -> None:
            """Добавляет три товара в корзину."""
            inventory_page = InventoryPage(self.driver)
            inventory_page.add_backpack() \
                .add_tshirt() \
                .add_onesie()

        @allure.step("Переход в корзину покупок")
        def go_to_cart() -> None:
            """Переходит на страницу корзины."""
            inventory_page = InventoryPage(self.driver)
            inventory_page.go_to_cart()

        @allure.step("Начало оформления заказа")
        def start_checkout() -> None:
            """Начинает процесс оформления заказа."""
            cart_page = CartPage(self.driver)
            cart_page.click_checkout()

        @allure.step("Заполнение формы личной информации")
        def fill_personal_info() -> None:
            """Заполняет форму личными данными покупателя."""
            checkout_page = CheckoutPage(self.driver)
            checkout_page.fill_personal_info("Иван", "Петров", "123456") \
                .click_continue()

        @allure.step("Получение итоговой суммы заказа")
        def get_total_amount() -> str:
            """Извлекает итоговую сумму со страницы подтверждения."""
            checkout_page = CheckoutPage(self.driver)
            return checkout_page.get_total_amount()

        @allure.step("Проверка итоговой суммы")
        def verify_total_amount(actual: str, expected: str) -> None:
            """
            Проверяет соответствие фактической суммы ожидаемой.

            Параметры:
                actual (str): Фактическая сумма
                expected (str): Ожидаемая сумма
            Возвращает:
                None
            """
            self.assertEqual(actual, expected,
                             f"Ожидаемая сумма: ${expected}, "
                             f"Фактическая сумма: ${actual}")

        # Выполнение шагов теста
        open_site()
        login()
        add_products()
        go_to_cart()
        start_checkout()
        fill_personal_info()

        total_amount = get_total_amount()
        expected_total = "58.29"

        verify_total_amount(total_amount, expected_total)

        with allure.step("Логирование успешного завершения теста"):
            print(f"Тест пройден успешно! Итоговая сумма: ${total_amount}")

    def tearDown(self) -> None:
        """
        Завершающие действия после каждого теста.

        Закрывает браузер и освобождает ресурсы.

        Параметры:
            Нет
        Возвращает:
            None
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()