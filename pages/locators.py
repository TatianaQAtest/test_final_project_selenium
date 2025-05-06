from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # в этом классе каждый селектор — это пара: как искать и что искать

class LoginPageLocators():
    LOGIN_LINK_LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_LINK_REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")