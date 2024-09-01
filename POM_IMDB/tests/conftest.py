import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()  # Initialize the Chrome webdriver
    driver.maximize_window()  # Maximize the browser window
    driver.get("https://www.imdb.com/search/name/")  # Open the website
    request.cls.driver = driver
    yield
    driver.quit()  # Close the WebDriver
