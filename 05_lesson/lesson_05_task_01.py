# lesson05_task1.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

def click_blue_button():
    # Настройка браузера Google Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Переход на страницу
        driver.get("http://uitestingplayground.com/classattr")
        
        # Даем странице время для загрузки
        time.sleep(5)
        
        # Поиск синей кнопки по классу 'btn-primary'
        blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        
        # Клик по синей кнопке
        blue_button.click()
        
        print("Успешно кликнули на синюю кнопку!")
        
        # Небольшая пауза чтобы увидеть результат
        time.sleep(5)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        
    finally:
        # Закрытие браузера
        driver.quit()

if __name__ == "__main__":
    click_blue_button()