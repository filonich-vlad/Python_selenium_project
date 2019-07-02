from selenium.webdriver.common.by import By


class MainPageLocators:
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_ADDED_TO_CART_ALERT = (By.CSS_SELECTOR, ".alert-success .alertinner")
    CART_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner")
    PRODUCT_NAME_IN_SUCCESS_ALERT = \
                        (By.CSS_SELECTOR, ".alert-success .alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
