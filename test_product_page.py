#from .pages.base_page import BasePage
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_cart(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.message_of_product_was_added_to_card()
    product_page.messege_of_price_of_the_cart_is_present()
    product_page.price_of_the_cart_coincides_with_the_price_of_the_product()
