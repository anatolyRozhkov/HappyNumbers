from selenium.webdriver.common.by import By
from tests.automation_tools.base_element import BaseElement as Be
from tests.automation_tools.base_page import BasePage as Bp
from tests.automation_tools.locator import Locator


class IndexPage(Bp):
    @property
    def authorize_link(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='li:nth-of-type(1) a'))

    @property
    def register_link(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='li:nth-of-type(2) a'))

    @property
    def meme_link(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='li:nth-of-type(3) a'))
