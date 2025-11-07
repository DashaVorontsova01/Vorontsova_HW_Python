# calculator_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):  # Добавлен конструктор с параметром driver
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

        # Локаторы
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CLASS_NAME, "screen")

        # Кнопки калькулятора
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_equals = (By.XPATH, "//span[text()='=']")

    def open(self):
        """Открыть страницу калькулятора"""
        self.driver.get(self.url)

    def set_delay(self, delay_value):
        """Установить значение задержки"""
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(delay_value))

    def click_button_7(self):
        """Нажать кнопку 7"""
        self.driver.find_element(*self.button_7).click()

    def click_button_8(self):
        """Нажать кнопку 8"""
        self.driver.find_element(*self.button_8).click()

    def click_plus(self):
        """Нажать кнопку +"""
        self.driver.find_element(*self.button_plus).click()

    def click_equals(self):
        """Нажать кнопку ="""
        self.driver.find_element(*self.button_equals).click()

    def get_screen_text(self):
        """Получить текст с экрана калькулятора"""
        return self.driver.find_element(*self.screen).text

    def wait_for_result(self, expected_result, timeout=46):
        """Ожидать появление ожидаемого результата"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(
            EC.text_to_be_present_in_element(self.screen, str(expected_result))
        )

    def perform_calculation(self, delay, num1, operator, num2):
        """Выполнить расчет с заданной задержкой"""
        self.set_delay(delay)

        # Нажимаем кнопки в зависимости от переданных параметров
        if num1 == 7:
            self.click_button_7()
        elif num1 == 8:
            self.click_button_8()

        if operator == '+':
            self.click_plus()

        if num2 == 7:
            self.click_button_7()
        elif num2 == 8:
            self.click_button_8()

        self.click_equals()