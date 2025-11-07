# test_calc.py
from selenium import webdriver
from calculator_page import CalculatorPage

def test_calculator_with_delay():
    # Инициализируем драйвер
    driver = webdriver.Chrome()

    try:
        # Создаем экземпляр Page Object
        calculator_page = CalculatorPage(driver)

        # Открываем страницу калькулятора
        calculator_page.open()

        # Вводим значение 45 в поле задержки
        calculator_page.set_delay(45)

        # Нажимаем кнопки: 7 + 8 = используя методы из класса
        calculator_page.click_button_7()  # Вместо click_button('7')
        calculator_page.click_plus()  # Вместо click_button('+')
        calculator_page.click_button_8()  # Вместо click_button('8')
        calculator_page.click_equals()  # Вместо click_button('=')

        # Ожидаем результат и проверяем его
        calculator_page.wait_for_result("15")

        # Проверяем окончательный результат
        result = calculator_page.get_screen_text()
        assert result == "15", f"Ожидался результат 15, но получили {result}"

        print("Тест успешно пройден! Результат 15 отобразился через 45 секунд.")

    finally:
        # Закрываем браузер
        driver.quit()

if __name__ == "main":
    test_calculator_with_delay()