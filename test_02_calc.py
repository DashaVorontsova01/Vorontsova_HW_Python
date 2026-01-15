from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator_with_delay():
    # Открываем браузер Google Chrome
    driver = webdriver.Chrome()

    try:
        # Открываем страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Вводим значение 45 в поле задержки
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажимаем кнопки: 7 + 8 =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Ожидаем появление результата 15 в течение 46 секунд (на 1 секунду больше чем задержка)
        wait = WebDriverWait(driver, 46)
        result_element = wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        # Проверяем, что результат отобразился
        screen_element = driver.find_element(By.CLASS_NAME, "screen")
        assert screen_element.text == "15", f"Ожидался результат 15, но получили {screen_element.text}"

        print("Тест успешно пройден! Результат 15 отобразился через 45 секунд.")

    finally:
        # Закрываем браузер
        driver.quit()


if __name__ == "main":
    test_calculator_with_delay()