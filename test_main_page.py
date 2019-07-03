import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    global link
    main_page = MainPage(browser, link) 
    main_page.open()
    main_page.should_be_login_link()
    main_page.go_to_login_page()
    login_page =  LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.basket
def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    global link
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty_text()
    basket_page.no_stuff_in_the_basket()
