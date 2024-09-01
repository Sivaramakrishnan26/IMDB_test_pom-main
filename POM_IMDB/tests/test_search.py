import pytest
from selenium import webdriver
from pages.search_page import SearchPage
import time


@pytest.mark.usefixtures("setup")
class TestSearch:  # Class for verifying search results on the IMDb Name Search page
    def test_search(self):
        time.sleep(5)
        search_page = SearchPage(self.driver)
        search_page.expand()
        search_page.enter_text("Walt Disney", "1901-01", "1901-12")
        search_page.see_results()
        time.sleep(5)
