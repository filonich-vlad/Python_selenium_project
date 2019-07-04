from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProfilePageLocators as PPL

class ProfilePage(BasePage):
    def should_be_profile_page(self):
        self.should_be_profile_page_url()
        self.should_be_delete_profile_button()

    def should_be_delete_profile_button(self):
        assert self.is_element_present(*PPL.DELETE_BUTTON), "No delete button."

    def should_by_profile_page_url(self):
        assert "/accounts/profile/" in self.browser.current_url

    def delete_profile(self):
        self.browser.find_element(*PPL.DELETE_BUTTON).click()
