import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators as PPL
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.profile_page import ProfilePage
from .pages.delete_profile_page import DeleteProfilePage
from faker import Faker


product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
links = [f"{product_link}/?promo=offer{i}" for i in range(10) if i != 7]

@pytest.mark.parametrize('link', links)
@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.message_of_product_was_added_to_card()
    product_page.product_name_in_message_is_the_same_as_one_in_the_cart()
    product_page.messege_of_price_of_the_cart_is_present()
    product_page.price_of_the_cart_coincides_with_the_price_of_the_product()


@pytest.mark.xfail(reason="Alert rises instantly.")
@pytest.mark.late
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    global product_link
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code(browser)
    product_page.is_not_element_present(*PPL.PRODUCT_ADDED_TO_CART_ALERT)

    
@pytest.mark.late
def test_guest_cant_see_success_message(browser):
    global product_link
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.is_not_element_present(*PPL.PRODUCT_ADDED_TO_CART_ALERT)
    

@pytest.mark.xfail(reason="The alert should stay.")
@pytest.mark.late
def test_message_dissapeared_after_adding_product_to_cart(browser):
    global product_link
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.is_disappeared(*PPL.PRODUCT_ADDED_TO_CART_ALERT)


@pytest.mark.login
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.login
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page =  LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.basket
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = product_link
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty_text()
    basket_page.no_stuff_in_the_basket()
        
@pytest.mark.login_user
class TestUserAddToCartFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        f = Faker()
        email = str(f.email())
        password = "asdfasdfa"
        self.browser = browser
        login_page = LoginPage(self.browser, login_link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        yield
        #We may end up on a random page, yet in order to avoid creating new
        #object, we will create profile page from the current url, then eill
        #go to the actual profile page.
        profile_page = ProfilePage(self.browser, self.browser.current_url)
        profile_page.go_to_profile_page()
        profile_page.delete_profile()
        delete_profile_page = DeleteProfilePage(self.browser, self.browser.current_url)
        delete_profile_page.confirm_delete(password)
        
    @pytest.mark.need_review    
    def test_user_can_add_product_to_cart(self):
        link = product_link
        product_page = ProductPage(self.browser, link)
        product_page.open()
        product_page.add_to_cart()
        product_page.message_of_product_was_added_to_card()
        product_page.product_name_in_message_is_the_same_as_one_in_the_cart()
        product_page.messege_of_price_of_the_cart_is_present()
        product_page.price_of_the_cart_coincides_with_the_price_of_the_product()


    def test_user_cant_see_success_message(self):
        global product_link
        product_page = ProductPage(self.browser, product_link)
        product_page.open()
        product_page.is_not_element_present(*PPL.PRODUCT_ADDED_TO_CART_ALERT)
