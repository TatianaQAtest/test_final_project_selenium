import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link_add', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", "offer7", "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, link_add):
    okay_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link_add}"

    page = ProductPage(browser, okay_link)
    page.open() 
    product_page = ProductPage(browser, browser.current_url)
    #browser.current_url - использует свойство Webdriver для проверки,что подстрока "login" есть в текущем url браузера. 
 
    product_page.add_to_basket()   
    product_page.solve_quiz_and_get_code()
    product_page.should_be_add_to_basket()
    
           