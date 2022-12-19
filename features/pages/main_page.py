from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from features.pages.base_page import Page


class MainPage(Page):
    # locator variables will be here
    CONTACT_TXT = (By.CSS_SELECTOR, ".footer-block__details-content.rte")
    SHOP_ALL_BTN = (By.CSS_SELECTOR, "a.header__menu-item.list-menu__item[href='/collections/all']")

    # methods for the main page will be here
    def open_main(self):
        self.open_url()

    def verify_contact_text(self, expected):
        self.verify_element_text(expected, *self.CONTACT_TXT)

    def click_shop_all(self):
        self.click(*self.SHOP_ALL_BTN)