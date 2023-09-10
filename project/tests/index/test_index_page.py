from tests.automation_tools.pages.authorization_page import AuthorizationPage
from tests.automation_tools.pages.index_page import IndexPage

from tests.automation_tools.pages.registration_page import RegistrationPage


def test_open_authorization_page(driver):
    """
    Open authorization page.
    """
    index_page = IndexPage(driver)
    authorization_page = AuthorizationPage(driver)

    index_page.go('https://hncom.github.io/qa-demo-test')

    index_page.authorize_link.click()

    assert authorization_page.email_field.exists()


def test_open_registration_page(driver):
    """
    Open authorization page.
    """
    index_page = IndexPage(driver)
    registration_page = RegistrationPage(driver)

    index_page.go('https://hncom.github.io/qa-demo-test')

    index_page.authorize_link.click()

    assert registration_page.email_field.exists()

