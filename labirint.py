from time import sleep  # импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

# зайти на сайт лабиринт
driver.get("https://www.labirint.ru/")

# найти книги по слову Питон
search_locator = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Python", Keys.RETURN)

# собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))

sleep(50)  # установили «засыпание» браузера на 50 секунд
