from tests.automation_tools.pages.registration_page import RegistrationPage


def test_name_field_activation(driver):
    """
   Name field becomes active upon selection.
    """
    registration_page = RegistrationPage(driver)

    registration_page.name_field.click()

    # assert registration_page.name_field.