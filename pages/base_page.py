from selenium.common.exceptions import NoSuchElementException, \
                                NoAlertPresentException, TimeoutException
from math import log, sin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        browser.implicitly_wait(timeout)
        self.browser = browser
        self.url = url

        
    def open(self):
        self.browser.get(self.url)


    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()



    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()


    def go_to_profile_page(self):
        self.browser.find_element(*BasePageLocators.ACCOUNT).click()
        
    

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False


    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
               "User icon is not presented, probably unauthorised user"


    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
               "Login link is not presented"

                
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
