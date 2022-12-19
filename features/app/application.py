from features.pages.cart_page import CartPage
from features.pages.main_page import MainPage
from features.pages.shop_page import ShopPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.cart_page = CartPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.shop_page = ShopPage(self.driver)
