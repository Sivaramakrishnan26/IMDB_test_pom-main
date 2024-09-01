from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):  # Method to find the element
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def scroll_to_element(self, locator, timeout=10):  # Method to scroll to the element
        element = self.find_element(locator, timeout)
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).perform()

    def click_element(self, locator, timeout=10):  # Method to click the element
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text, timeout=20):  # Method to Send Keys to the element
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
