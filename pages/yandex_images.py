from pages.base import BasePage
from selenium.webdriver.common.by import By


# Page Object for yandex.ru/images
class ImagesPage(BasePage):
    locator_category = (By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    locator_text = (By.CLASS_NAME, "input__control")
    locator_first_image = (By.CLASS_NAME, "serp-item_pos_0")
    locator_btn_next = (By.CLASS_NAME, "CircleButton_type_next")
    locator_btn_prev = (By.CLASS_NAME, "CircleButton_type_prev")
    locator_media_viewer = (By.CLASS_NAME, "Modal")
    locator_current_image = (By.CLASS_NAME, "MMImage-Preview")

    def get_first_category(self):
        return self.find_element(self.locator_category)

    def get_first_image(self):
        return self.find_element(self.locator_first_image)

    def get_text(self):
        return self.find_element(self.locator_text)

    def get_media_viewer(self):
        return self.find_element(self.locator_media_viewer)

    def get_current_image(self):
        return self.find_element(self.locator_current_image)

    def click_button_next(self):
        return self.find_element(self.locator_btn_next).click()

    def click_button_prev(self):
        return self.find_element(self.locator_btn_prev).click()
