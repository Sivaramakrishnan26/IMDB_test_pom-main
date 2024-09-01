from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.common.exceptions import ElementClickInterceptedException
import time


class SearchPage(BasePage):
    EXPAND_ALL = (By.XPATH, "//span[text()='Expand all']")
    NAME = (By.XPATH, "//input[@aria-label='Name']")
    BIRTH_DATE_FROM = (By.ID, "text-input__10")
    BIRTH_DATE_TO = (By.ID, "text-input__11")
    SEE_RESULTS = (By.XPATH, "//span[text()='See results']")

    def expand(self):  # Method to scroll to expand and click it
        try:
            self.find_element(self.EXPAND_ALL)
            self.scroll_to_element(self.EXPAND_ALL)
            self.click_element(self.EXPAND_ALL)
        except MoveTargetOutOfBoundsException as e:
            print(f"Exception Occurred: {e}")
        except ElementClickInterceptedException as e:
            print(f"Exception Occurred: {e}")

    def enter_text(self, name, birth_date_from, birth_date_to):  # Method to send keys to the element
        self.find_element(self.NAME)
        self.scroll_to_element(self.NAME)
        self.send_keys(self.NAME, name)
        self.find_element(self.BIRTH_DATE_FROM)
        self.scroll_to_element(self.BIRTH_DATE_FROM)
        self.send_keys(self.BIRTH_DATE_FROM, birth_date_from)
        self.find_element(self.BIRTH_DATE_TO)
        self.scroll_to_element(self.BIRTH_DATE_TO)
        self.send_keys(self.BIRTH_DATE_TO, birth_date_to)

    def see_results(self):  # Method to See results
        try:
            time.sleep(2)
            self.find_element(self.SEE_RESULTS)
            self.scroll_to_element(self.SEE_RESULTS)
            self.click_element(self.SEE_RESULTS)
        except ElementClickInterceptedException as e:
            print(f"Exception Occurred: {e}")
