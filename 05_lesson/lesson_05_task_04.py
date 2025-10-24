# lesson05_task4.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открыть браузер FireFox
driver = webdriver.Firefox()

try:
    # Перейти на страницу http://the-internet.herokuapp.com/login
    driver.get("http://the-internet.herokuapp.com/login")
    
    # В поле username ввести значение tomsmith
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    
    # В поле password ввести значение SuperSecretPassword
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword")
    
    # Нажать кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    # Небольшая пауза для загрузки страницы
    time.sleep(2)
    
    # Вывести текст с зеленой плашки в консоль
    success_message = driver.find_element(By.ID, "flash")
    print("Текст с зеленой плашки:", success_message.text)
    
    # Небольшая пауза для демонстрации
    time.sleep(2)

finally:
    # Закрыть браузер (метод quit())
    driver.quit()