from .base_page import BasePage
from .locators import BasketPageLocators as BPL


class BasketPage(BasePage):

    
    def basket_is_empty_text(self):
        assert "Your basket is empty." in \
               self.browser.find_element(*BPL.BASKET_IS_EMPTY_TEXT).text, \
               "No message of empty basket."

    def no_stuff_in_the_basket(self):
        assert not self.is_element_present(*BPL.BASKET_SET), \
               "Basket in not empty, though it should be."
