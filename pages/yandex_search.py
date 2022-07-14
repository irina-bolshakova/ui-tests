from pages.base import BasePage
from selenium.webdriver.common.by import By


# Page Object for yandex.ru/search
class SearchPage(BasePage):
    locator_search_result = (By.ID, "search-result")
    locator_results = (By.CSS_SELECTOR, ".main__content li.serp-item div.organic a.organic__url")

    def get_search_result(self):
        return self.find_element(self.locator_search_result)

    def get_results(self):
        return self.find_elements(self.locator_results)
