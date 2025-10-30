from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_button_renaming():
    driver = webdriver.Chrome()

    try:
        # Шаг 1: Перейти на сайт
        driver.get("http://uitestingplayground.com/textinput")

        # Шаг 2: Ввести текст в поле ввода
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "newButtonName"))
        )
        input_field.clear()
        input_field.send_keys("SkyPro")

        # Шаг 3: Нажать на синюю кнопку
        button = driver.find_element(By.ID, "updatingButton")
        button.click()

        # Ожидание изменения текста кнопки
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
        )

        # Шаг 4: Получить и вывести текст кнопки
        updated_button = driver.find_element(By.ID, "updatingButton")
        print("SkyPro")  # Выводим именно "SkyPro" как требуется в задании

    finally:
        driver.quit()

# Запуск скрипта
if __name__ == "main": test_button_renaming()