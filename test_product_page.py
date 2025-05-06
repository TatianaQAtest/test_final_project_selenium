
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    # Задание: добавление в корзину со страницы товара
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    page = ProductPage(browser, link)
    page.open() 
    product_page = ProductPage(browser, browser.current_url)  
    product_page.add_to_basket()
   
    product_page.solve_quiz_and_get_code()
    product_page.should_be_add_to_basket()

 