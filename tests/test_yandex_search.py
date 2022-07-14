import time
from pages.yandex import MainPage
from pages.yandex_search import SearchPage


# Проверка сценария "Поиск в яндексе"
def test_search(browser):
    page = MainPage(browser)
    page.go_to_site()
    assert page.get_search_field() is not None
    page.enter_word('Тензор')
    time.sleep(2)
    assert page.get_suggest() is not None
    page.press_enter()
    page = SearchPage(browser)
    time.sleep(5)
    assert page.get_search_result() is not None
    links = page.get_results()
    url = links[0].get_attribute('href')
    assert url == 'https://tensor.ru/'
