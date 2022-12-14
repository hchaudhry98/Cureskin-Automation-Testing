from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from features.pages.base_page import Page


class CartPage(Page):
    # locator variables to be initialized here
    CONT_SHOP_BTN = (By.CSS_SELECTOR, ".cart__warnings a[href='/collections/all']")
    CART_BTN = (By.ID, 'cart-icon-bubble')

    # functions that usually are needed for the cart page will appear here
    def open_cart(self):
        self.open_url('/cart')

    def click_continue_shopping(self):
        self.click(*self.CONT_SHOP_BTN)

    def verify_url_contains(self, query):
        self.verify_url_contains_query(query)
