from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time


class BaseElement:
    def __init__(self, driver, locator, wait_time=3):
        self.driver = driver
        self.locator = locator
        self.wait_time = wait_time

        self.web_element = None
        self.find()

    def find(self) -> None:

        try:
            element = WebDriverWait(self.driver, self.wait_time).until(
                ec.presence_of_element_located(locator=self.locator))

            self.web_element = element
        except TimeoutException:
            pass

    def click(self) -> None:
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(self.locator), ec.staleness_of(self.locator))
        element.click()

    def press_enter(self) -> None:
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(self.locator))
        element.send_keys(Keys.RETURN)

    def input_text(self, text: str) -> None:
        element = WebDriverWait(self.driver, self.wait_time).until(
            ec.element_to_be_clickable(self.locator))
        element.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        element.send_keys(text)

    def attach_file(self, file_path: str) -> None:
        self.web_element.send_keys(file_path)

    @property
    def text(self) -> str:
        text = self.web_element.text
        return text

    def has_class(self, class_name: str) -> bool:
        classes = self.web_element.get_attribute("class")
        if classes:
            return class_name in classes.split()
        return False

    def attribute_by_name(self, attr_name: str) -> str:
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    def has_attribute(self, attr_name: str) -> bool:
        inner_html = self.attribute_by_name("innerHTML")
        if attr_name in inner_html:
            return True
        else:
            return False

    def is_visible(self) -> bool:
        if self.web_element is not None:
            try:
                visibility = WebDriverWait(self.driver, self.wait_time).until(
                    ec.visibility_of_element_located(self.locator))
            except TimeoutException:
                visibility = False

            return visibility
        else:
            return False

    def exists(self) -> bool:
        if self.web_element is not None:
            return True
        else:
            return False

    def is_not_visible(self) -> bool:
        if self.web_element is not None:
            try:
                visibility = WebDriverWait(self.driver, self.wait_time).until(
                    ec.invisibility_of_element_located(self.locator))
            except TimeoutException:
                visibility = False

            return visibility
        else:
            return True
