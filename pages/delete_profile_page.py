from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import DeleteProfilePageLocators as DPPL


class DeleteProfilePage(BasePage):
    def confirm_delete(self, password):
        self.browser.find_element(*DPPL.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*DPPL.DELETE_BUTTON).click()
