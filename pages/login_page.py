from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, \
                               "url doesn't contain \"\login\""

    def should_be_login_form(self):
        assert is_element_present(*LoginPageLocators.LOGIN_FORM), \
                               "No login form found"

    def should_be_register_form(self):
        assert is_element_present(*LoginPageLocaors.REGISTER_FORM), \
                               "No register form found"
