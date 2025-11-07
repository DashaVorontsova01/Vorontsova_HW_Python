from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        )
        username_input.send_keys(username)
        return self

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.password_field)
        password_input.send_keys(password)
        return self

    def click_login(self):
        login_btn = self.driver.find_element(*self.login_button)
        login_btn.click()
        return self