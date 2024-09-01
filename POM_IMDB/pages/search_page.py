from selenium.webdriver.common.by import By
from .base_page import BasePage
import time
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.common.exceptions import ElementClickInterceptedException


class SearchPage(BasePage):
    EXPAND_ALL = (By.XPATH, "//span[text()='Expand all']")
    NAME = (By.XPATH, "//input[@aria-label='Name']")
    SEE_RESULTS = (By.XPATH, "//span[text()='See results']")

    def scroll(self):  # Method to scroll to the element
        try:
            self.find_element(self.EXPAND_ALL)
            self.scroll_to_element(self.EXPAND_ALL)
        except MoveTargetOutOfBoundsException as e:
            print(f"Exception Occurred: {e}")

    def click(self):  # Method to click the element
        try:
            time.sleep(2)
            self.click_element(self.EXPAND_ALL)
        except ElementClickInterceptedException as e:
            print(f"Exception Occurred: {e}")

    def enter_name(self, name):  # Method to send keys to the element
        self.find_element(self.NAME)
        self.scroll_to_element(self.NAME)
        self.send_keys(self.NAME, name)

    def see_results(self):  # Method to See results
        try:
            self.click_element(self.SEE_RESULTS)
            print("Clicked on SEE_RESULTS button")
        except ElementClickInterceptedException as e:
            print(f"Exception Occurred: {e}")
