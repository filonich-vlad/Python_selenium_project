from .base_page import BasePage
from .locators import ProductPageLocators as PPL

class ProductPage(BasePage): 

    def add_to_cart(self):
        self.browser.find_element(*PPL.ADD_TO_CART_BUTTON).click()

    def message_of_product_was_added_to_card(self):
        assert "has been added to your basket" in \
               self.browser.find_element(*PPL.PRODUCT_ADDED_TO_CART_MESSAGE).text,\
               "No product name in message of product being added to the cart or no message at all."
    
    def product_name_in_message_is_the_same_as_one_in_the_cart(self):
        PRODUCT_NAME = self.browser.find_element(*PPL.PRODUCT_NAME).text
        ALERT = self.browser.find_element(*PPL.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text
        assert PRODUCT_NAME == ALERT, "Product name is not found in succes alert."
                           

    def messege_of_price_of_the_cart_is_present(self):
        assert self.is_element_present(*PPL.CART_PRICE), "No cart price message found."

    def price_of_the_cart_coincides_with_the_price_of_the_product(self):
        PRODUCT_PRICE = self.browser.find_element(*PPL.PRODUCT_PRICE).text
        ALERT = self.browser.find_element(*PPL.CART_PRICE).text
        assert PRODUCT_PRICE in ALERT, "Price of the cart != price of the product"
