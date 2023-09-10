from selenium.webdriver.common.by import By
from tests.automation_tools.base_element import BaseElement as Be
from tests.automation_tools.base_page import BasePage as Bp
from tests.automation_tools.locator import Locator


class RegistrationPage(Bp):
    @property
    def name_field(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='input[name="name"]'))

    @property
    def role_dropdown(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='select'))

    def role_dropdown_option(self, option):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value=f'select option:nth-child({option})'))

    @property
    def email_field(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='input[name="email"]'))

    @property
    def password_field(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='input[name="password"]'))

    @property
    def confirm_password_field(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='input[name="confirm-password"]'))

    @property
    def terms_and_conditions_checkbox(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='label[name="agree-terms"]'))

    @property
    def marketing_emails_checkbox(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='label[name="agree-marketing"]'))

    @property
    def register_button(self):
        return Be(driver=self.driver, locator=Locator(by=By.CSS_SELECTOR, value='button'))

    """
    Error messages.
    """

    @property
    def type_your_name_message(self):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH, value="//span[contains(text(), 'Type your name')]"))

    @property
    def you_have_to_choose_role_message(self):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH,
                                                      value="//span[contains(text(), 'You have to chosen role')]"))

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

    @property
    def confirm_the_password_message(self):
        return Be(driver=self.driver, locator=Locator(by=By.XPATH,
                                                      value="//span[contains(text(), 'Confirm the password')]"))
