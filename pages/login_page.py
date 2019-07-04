from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators as LPL
from selenium.common.exceptions import NoAlertPresentException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, \
                               "url doesn't contain \"/login\""

    def should_be_login_form(self):
        assert self.is_element_present(*LPL.LOGIN_FORM), \
                               "No login form found"

    def should_be_register_form(self):
        assert self.is_element_present(*LPL.REGISTER_FORM), \
                               "No register form found"


    def register_new_user(self, email, password):
        self.browser.find_element(*LPL.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LPL.REG_PASSWORD).send_keys(password)
        self.browser.find_element(*LPL.REG_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LPL.REGISTRATION_SUBMIT_BUTTON).click()
        
