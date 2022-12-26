from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from features.pages.base_page import Page


class ShopPage(Page):
    # locator variables will be here
    PRODUCTS = (By.CSS_SELECTOR, ".full-unstyled-link")
    PAGE_2 = (By.CSS_SELECTOR, "a.pagination__item[aria-label='Page 2']")

    # methods will go here
    def click_page_2(self):
        self.wait_for_element_appear(*self.PAGE_2)
        self.click(*self.PAGE_2)

    def get_all_products(self):
        products = self.find_elements(*self.PRODUCTS)
        check = True
        for product in products:
            if 'test' in product.text.lower():
                check = False

        assert check, f'Test product found'

