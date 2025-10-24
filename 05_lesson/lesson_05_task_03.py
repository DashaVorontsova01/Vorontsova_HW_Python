from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открыть браузер FireFox
driver = webdriver.Firefox()

try:
    # Перейти на страницу
    driver.get("http://the-internet.herokuapp.com/inputs")
    
    # Найти поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")
    
    # Ввести в поле текст Sky
    input_field.send_keys("Sky")
    
    # Небольшая пауза для наглядности
    time.sleep(1)
    
    # Очистить это поле
    input_field.clear()
    
    # Небольшая пауза для наглядности
    time.sleep(1)
    
    # Ввести в поле текст Pro
    input_field.send_keys("Pro")
    
    # Небольшая пауза чтобы увидеть результат
    time.sleep(2)

finally:
    # Закрыть браузер
    driver.quit()