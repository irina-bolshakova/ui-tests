from pages.base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


# Page Object for yandex.ru
class MainPage(BasePage):
    locator_search_field = (By.ID, "text")
    locator_suggest = (By.CLASS_NAME, "mini-suggest__popup")
    locator_images = (By.CSS_SELECTOR, "a[data-id='images']")

    def get_search_field(self):
        return self.find_element(self.locator_search_field)

    def get_suggest(self):
        return self.find_element(self.locator_suggest)

    def get_images(self):
        return self.find_element(self.locator_images)

    def enter_word(self, word):
        search_field = self.find_element(self.locator_search_field)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def press_enter(self):
        search_field = self.find_element(self.locator_search_field)
        search_field.click()
        search_field.send_keys(Keys.ENTER)
        return search_field
