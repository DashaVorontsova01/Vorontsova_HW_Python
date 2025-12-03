from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt_add_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_add_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack(self):
        backpack_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.backpack_add_button)
        )
        backpack_btn.click()
        return self

    def add_tshirt(self):
        tshirt_btn = self.driver.find_element(*self.tshirt_add_button)
        tshirt_btn.click()
        return self

    def add_onesie(self):
        onesie_btn = self.driver.find_element(*self.onesie_add_button)
        onesie_btn.click()
        return self

    def go_to_cart(self):
        cart_btn = self.driver.find_element(*self.cart_icon)
        cart_btn.click()
        return self