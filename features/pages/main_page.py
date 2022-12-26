from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from features.pages.base_page import Page


class MainPage(Page):
    # locator variables will be here
    HAM_MENU = (By.CSS_SELECTOR, ".icon.icon-hamburger")
    CONTACT_TXT = (By.CSS_SELECTOR, ".footer-block__details-content.rte")
    # SHOP_ALL_BTN = (By.CSS_SELECTOR, "a.header__menu-item.list-menu__item[href='/collections/all']")
    HAM_SHOP_ALL = (By.CSS_SELECTOR, "a.menu-drawer__menu-item[href='/collections/all']")

    # methods for the main page will be here
    def open_main(self):
        self.open_url()

    def verify_contact_text(self, expected):
        self.verify_element_text(expected, *self.CONTACT_TXT)

    def click_shop_all(self):
        self.click_ham()
        self.wait_for_element_appear(*self.HAM_SHOP_ALL)
        self.click(*self.HAM_SHOP_ALL)

    def click_ham(self):
        # If Hamburger Menu is visible
        self.wait_for_element_appear(*self.HAM_MENU)
        self.click(*self.HAM_MENU)