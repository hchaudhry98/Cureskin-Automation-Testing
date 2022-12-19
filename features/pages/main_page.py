from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from features.pages.base_page import Page


class MainPage(Page):
    # locator variables will be here
    CONTACT_TXT = (By.CSS_SELECTOR, ".footer-block__details-content.rte")

    # methods for the main page will be here
    def open_main(self):
        self.open_url()

    def verify_contact_text(self, expected):
        self.verify_element_text(expected, *self.CONTACT_TXT)
