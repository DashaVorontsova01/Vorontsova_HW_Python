from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_personal_info(self, firstname, lastname, postal_code):
        first_name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.first_name_field)
        )
        first_name_input.send_keys(firstname)

        last_name_input = self.driver.find_element(*self.last_name_field)
        last_name_input.send_keys(lastname)

        postal_code_input = self.driver.find_element(*self.postal_code_field)
        postal_code_input.send_keys(postal_code)
        return self

    def click_continue(self):
        continue_btn = self.driver.find_element(*self.continue_button)
        continue_btn.click()
        return self

    def get_total_amount(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total_label)
        )
        total_text = total_element.text
        total_amount = total_text.split("$")[1]
        return total_amount