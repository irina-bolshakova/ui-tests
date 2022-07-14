import time
from pages.yandex import MainPage
from pages.yandex_images import ImagesPage


# Проверка сценария "Картинки на яндексе"
def test_search_images(browser):
    page = MainPage(browser)
    page.go_to_site()
    images = page.get_images()
    assert images is not None
    images.click()
    page = ImagesPage(browser)
    page.switch_tab(1)
    assert page.driver.current_url == 'https://yandex.ru/images/?utm_source=main_stripe_big'  #'https://yandex.ru/images/'
    text = page.get_first_category().get_attribute('data-grid-text')
    page.get_first_category().click()
    time.sleep(2)
    assert text == page.get_text().get_attribute('value')
    page.get_first_image().click()
    time.sleep(2)
    assert page.get_media_viewer().is_displayed()
    img_1 = page.get_current_image().get_attribute('src')
    page.click_button_next()
    time.sleep(2)
    img_2 = page.get_current_image().get_attribute('src')
    assert img_2 != img_1
    page.click_button_prev()
    time.sleep(2)
    img_3 = page.get_current_image().get_attribute('src')
    assert img_3 == img_1

