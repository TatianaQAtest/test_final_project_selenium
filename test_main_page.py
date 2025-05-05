from .pages.main_page import MainPage

# Запуск теста: pytest -v --tb=line --language=en test_main_page.py 
# (если Bash открыт в директории, где сам файл test_main_page.py или указать полный путь к нему)

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
 
    page.open()
    # открываем страницу

    page.go_to_login_page()
    # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
# добавляем тест
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()