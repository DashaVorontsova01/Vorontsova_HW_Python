from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # 1. Переход на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # 2. Ожидаем загрузки конкретно третьего изображения
    wait = WebDriverWait(driver, 15)

    # Ждем пока загрузится третье изображение (по индексу или атрибуту)
    third_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#image-container img:nth-child(3)")))

    # 3. Получаем атрибут src
    src_attribute = third_image.get_attribute("src")

    # 4. Вывод значения в консоль
    print(f"SRC атрибут третьей картинки: {src_attribute}")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()