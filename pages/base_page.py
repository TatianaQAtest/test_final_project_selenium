from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
    # Конструктор __init__ — метод, который вызывается, когда мы создаем объект
    # В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
        self.browser = browser
        self.url = url 
        self.browser.implicitly_wait(timeout)

    def open(self): 
    # Метод open открывает нужную страницу в браузере, используя метод get() - переход по ссылке
        self.browser.get(self.url)

    def is_element_present(self, how, what):
    # Добавили метод is_element_present, в котором будем перехватывать исключение(с помощью конструкции try/except).
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
    # Считаем математическое выражение - метод для получения проверочного кода
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")   
        