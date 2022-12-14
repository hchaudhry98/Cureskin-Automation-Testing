from features.pages.cart_page import CartPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.cart_page = CartPage(self.driver)
