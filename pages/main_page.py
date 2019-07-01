from .base_page import BasePage
from .locators import MainPageLocators as MPL

class MainPage(BasePage):

    def should_be_login_link(self):
        assert self.is_element_present(*MPL.LOGIN_LINK), \
                                       "Login link is not present"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MPL.LOGIN_LINK)
        login_link.click()

