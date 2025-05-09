import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


@pytest.mark.skip  
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#Проверяем (с помощью is_not_element_present), что нет сообщения об успехе после добавления товара в корзину   
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)        
    product_page.add_to_basket()
    time.sleep(1)
    product_page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):  
#Проверяем (с помощью is_not_element_present), что нет сообщения об успехе после того, как открыли страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open() 
    product_page = ProductPage(browser, browser.current_url)
    time.sleep(1)   
    product_page.should_not_be_success_message()

@pytest.mark.skip    
def test_message_disappeared_after_adding_product_to_basket(browser):
#Проверяем (с помощью is_disappeared), что нет сообщения об успехе после добавления товара в корзину 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open() 
    product_page = ProductPage(browser, browser.current_url)       
    product_page.add_to_basket()
    time.sleep(1)
    product_page.should_be_success_message() 

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
#Тест: гость видит ссылку login_link на странице продукта"
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()        
    page.should_be_login_link() 
  
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
#Тест: гость может перейти на страницу логина со страницы продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()    
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
# для задания: наследование и отрицательные проверки
# 1 Гость открывает страницу товара 
# 2 Переходит в корзину по кнопке в шапке сайта
# 3 Ожидаем, что в корзине нет товаров
# 4 Ожидаем, что есть текст о том что корзина пуста 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open() 

    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)\
    # Создаем экземпляр страницы корзины, присваиваем ее переменной basket_page
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()
