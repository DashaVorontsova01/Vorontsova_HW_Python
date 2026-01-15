from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_validation():
    # Инициализация драйвера Edge с опциями
    options = webdriver.EdgeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Edge(options=options)

    try:
        print("Открываем страницу...")
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Ждем загрузки страницы
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        print("Заполняем форму...")
        # Данные для заполнения
        fields_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        # Заполняем все поля кроме zip-code
        for field_name, value in fields_data.items():
            field = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.NAME, field_name))
            )
            field.clear()
            field.send_keys(value)
            print(f"Заполнено поле {field_name}")

        # Явно очищаем zip-code (оставляем пустым)
        zip_field = driver.find_element(By.NAME, "zip-code")
        zip_field.clear()
        print("Поле zip-code оставлено пустым")

        # Нажимаем кнопку Submit
        print("Нажимаем кнопку Submit...")
        submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
        submit_btn.click()

        # Ждем когда применится валидация
        print("Ждем применения валидации...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name='zip-code'].is-invalid"))
        )

        # Проверяем поле zip-code (должно быть красным)
        print("Проверяем поле zip-code...")
        zip_element = driver.find_element(By.NAME, "zip-code")
        zip_classes = zip_element.get_attribute("class")
        print(f"Классы zip-code: {zip_classes}")

        # Проверяем наличие класса указывающего на ошибку
        assert "is-invalid" in zip_classes, f"Поле zip-code должно иметь класс is-invalid. Текущие классы: {zip_classes}"

        # Проверяем остальные поля (должны быть зелеными)
        print("Проверяем остальные поля...")
        for field_name in fields_data.keys():
            field_element = driver.find_element(By.NAME, field_name)
            field_classes = field_element.get_attribute("class")
            print(f"Классы {field_name}: {field_classes}")

            assert "is-valid" in field_classes, f"Поле {field_name} должно иметь класс is-valid. Текущие классы: {field_classes}"

        print("✓ ТЕСТ ПРОЙДЕН УСПЕШНО!")
        print("✓ Поле zip-code подсвечено красным")
        print("✓ Все остальные поля подсвечены зеленым")

    except Exception as e:
        print(f"✗ ОШИБКА: {e}")
        # Сохраняем скриншот и HTML для отладки
        driver.save_screenshot("debug_screenshot.png")
        with open("debug_page.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("Скриншот сохранен как: debug_screenshot.png")
        print("HTML страницы сохранен как: debug_page.html")
        raise
    finally:
        print("Закрываем браузер...")
        driver.quit()

if __name__ == "main":
    test_form_validation()