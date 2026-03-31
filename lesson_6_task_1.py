from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

try:
    # Нажимаем на синюю кнопку
    driver.find_element(By.ID, "ajaxButton").click()

    # Ждем появления зеленого текста и получаем его
    success_text = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    # Выводим текст в консоль
    print(success_text.text)

finally:
    driver.quit()