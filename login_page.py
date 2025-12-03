"""
Модуль содержит классы Page Object для страниц сайта.
Каждый класс инкапсулирует взаимодействие с элементами конкретной страницы.
"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Page Object класс для страницы авторизации.

    Атрибуты:
        driver (WebDriver): Экземпляр веб-драйвера для взаимодействия с браузером
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует экземпляр LoginPage.

        Параметры:
            driver (WebDriver): Экземпляр веб-драйвера
        Возвращает:
            None
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username: str) -> 'LoginPage':
        """
        Вводит имя пользователя в поле ввода.

        Параметры:
            username (str): Имя пользователя для авторизации
        Возвращает:
            LoginPage: Текущий экземпляр класса для цепочки вызовов
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        return self

    def enter_password(self, password: str) -> 'LoginPage':
        """
        Вводит пароль в поле ввода.

        Параметры:
            password (str): Пароль для авторизации
        Возвращает:
            LoginPage: Текущий экземпляр класса для цепочки вызовов
        """
        self.driver.find_element(*self.password_input).send_keys(password)
        return self

    def click_login(self) -> None:
        """
        Нажимает кнопку входа в систему.

        Параметры:
            Нет
        Возвращает:
            None
        """
        self.driver.find_element(*self.login_button).click()


class InventoryPage:
    """
    Page Object класс для страницы с товарами (инвентаря).

    Атрибуты:
        driver (WebDriver): Экземпляр веб-драйвера
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует экземпляр InventoryPage.

        Параметры:
            driver (WebDriver): Экземпляр веб-драйвера
        Возвращает:
            None
        """
        self.driver = driver
        self.backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self) -> 'InventoryPage':
        """
        Добавляет рюкзак в корзину.

        Параметры:
            Нет
        Возвращает:
            InventoryPage: Текущий экземпляр класса для цепочки вызовов
        """
        self.driver.find_element(*self.backpack_button).click()
        return self

    def add_tshirt(self) -> 'InventoryPage':
        """
        Добавляет футболку в корзину.

        Параметры:
            Нет
        Возвращает:
            InventoryPage: Текущий экземпляр класса для цепочки вызовов
        """
        self.driver.find_element(*self.tshirt_button).click()
        return self

    def add_onesie(self) -> 'InventoryPage':
        """
        Добавляет комбинезон в корзину.

        Параметры:
            Нет
        Возвращает:
            InventoryPage: Текущий экземпляр класса для цепочки вызовов
        """
        self.driver.find_element(*self.onesie_button).click()
        return self

    def go_to_cart(self) -> None:
        """
        Переходит в корзину покупок.

        Параметры:
            Нет
        Возвращает:
            None
        """
        self.driver.find_element(*self.cart_icon).click()


class CartPage:
    """
    Page Object класс для страницы корзины покупок.

    Атрибуты:
        driver (WebDriver): Экземпляр веб-драйвера
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует экземпляр CartPage.

        Параметры:
            driver (WebDriver): Экземпляр веб-драйвера
        Возвращает:
            None
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа.

        Параметры:
            Нет
        Возвращает:
            None
        """
        self.driver.find_element(*self.checkout_button).click()


class CheckoutPage:
    """
    Page Object класс для страницы оформления заказа.

    Атрибуты:
        driver (WebDriver): Экземпляр веб-драйвера
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует экземпляр CheckoutPage.

        Параметры:
            driver (WebDriver): Экземпляр веб-драйвера
        Возвращает:
            None
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_amount_label = (By.CLASS_NAME, "summary_total_label")

    def fill_personal_info(self, first_name: str, last_name: str,
                          postal_code: str) -> 'CheckoutPage':
        """
        Заполняет форму личной информации.

        Параметры:
            first_name (str): Имя покупателя
            last_name (str): Фамилия покупателя
            postal_code (str): Почтовый индекс
        Возвращает:
            CheckoutPage: Текущий экземпляр класса для цепочки вызовов
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        return self

    def click_continue(self) -> None:
        """
        Нажимает кнопку продолжения оформления заказа.

        Параметры:
            Нет
        Возвращает:
            None
        """
        self.driver.find_element(*self.continue_button).click()

    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа со страницы.

        Параметры:
            Нет
        Возвращает:
            str: Итоговая сумма в текстовом формате
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_amount_label)
        )
        total_text = self.driver.find_element(*self.total_amount_label).text
        return total_text.split("$")[1]