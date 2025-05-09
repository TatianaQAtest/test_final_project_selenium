import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

# Запуск теста: pytest -v --tb=line --language=en test_main_page.py 
# (если Bash открыт в директории, где сам файл test_main_page.py или указать полный путь к нему)

@pytest.mark.skip 
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
 
    page.open()
    # открываем страницу

    page.go_to_login_page()
    # выполняем метод страницы — переходим на страницу логина

@pytest.mark.skip 
def test_guest_should_see_login_link(browser):
# добавляем тест
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
# для задания: наследование и отрицательные проверки
# 1 Гость открывает главную страницу 
# 2 Переходит в корзину по кнопке в шапке сайта
# 3 Ожидаем, что в корзине нет товаров
# 4 Ожидаем, что есть текст о том что корзина пуста 
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()    

    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()