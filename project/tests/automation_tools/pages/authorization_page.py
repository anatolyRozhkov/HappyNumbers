from selenium.webdriver.common.by import By
from tests.automation_tools.base_element import BaseElement as Be
from tests.automation_tools.base_page import BasePage as Bp
from tests.automation_tools.locator import Locator


class AuthorizationPage(Bp):
    @property
    def email_field(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='input[name="email"]'))

    @property
    def password_field(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='input[name="password"]'))

    @property
    def authorize_button(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='button'))

    """
    Error messages.
    """

    @property
    def enter_your_email_message(self):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH,
                                                      value="//span[contains(text(), 'Enter your email')]"))


    @property
    def at_symbol_message(self):
        return Be(driver=self.driver, locator=Locator(
            by=By.XPATH,
            value="//span[contains(text(), 'Please include '@' in the email address')]"))


    @property
    def part_after_at_symbol_message(self):
        return Be(driver=self.driver, locator=Locator(
            by=By.XPATH,
            value="//span[contains(text(), 'Please enter a part following '@'')]"))


    @property
    def please_enter_a_domain_message(self):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH,
                                                      value="//span[contains(text(), 'Please enter a domain')]"))


    @property
    def enter_your_password_message(self):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH,
                                                      value="//span[contains(text(), 'Enter your password')]"))
