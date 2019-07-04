from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.LINK_TEXT, "View basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    ACCOUNT = (By.CSS_SELECTOR, "[href=\"/en-gb/accounts/\"]")
    

class MainPageLocators:
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name=\"registration_submit\"]")
    

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_ADDED_TO_CART_ALERT = (By.CSS_SELECTOR, ".alert-success .alertinner")
    CART_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner")
    PRODUCT_NAME_IN_SUCCESS_ALERT = \
                        (By.CSS_SELECTOR, ".alert-success .alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")

class BasketPageLocators:
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_SET = (By.CSS_SELECTOR, "#basket_formset")

class ProfilePageLocators:
    DELETE_BUTTON = (By.CSS_SELECTOR, "#delete_profile")

class DeleteProfilePageLocators:
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_password")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".btn-danger")
