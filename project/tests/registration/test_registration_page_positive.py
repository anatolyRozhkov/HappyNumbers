from faker import Faker

from tests.automation_tools.pages.index_page import IndexPage
from tests.automation_tools.pages.registration_page import RegistrationPage

fake = Faker()


def test_name_field(driver):
    """
    Test name field.
    """
    # When
    index_page = IndexPage(driver)
    registration_page = RegistrationPage(driver)

    index_page.go('https://hncom.github.io/qa-demo-test')

    index_page.register_link.click()

    dummy_text = fake.sentence()

    registration_page.name_field.input_text(dummy_text)

    # Then

    # Verify that error messages are hidden
    assert registration_page.type_your_name_message.is_not_visible()
    assert registration_page.you_have_to_choose_role_message.is_not_visible()
    assert registration_page.enter_your_email_message.is_not_visible()
    assert registration_page.enter_your_password_message.is_not_visible()
    assert registration_page.confirm_the_password_message.is_not_visible()

    # Verify that red validation did not kick in
    assert not registration_page.name_field.has_class('input-error')
    assert not registration_page.role_dropdown.has_class('select-error')
    assert not registration_page.email_field.has_class('input-error')
    assert not registration_page.password_field.has_class('input-error')
    assert not registration_page.confirm_password_field.has_class('input-error')


def test_role_dropdown(driver):
    """
    Test role dropdown.
    """
    # When
    index_page = IndexPage(driver)
    registration_page = RegistrationPage(driver)

    index_page.go('https://hncom.github.io/qa-demo-test')

    index_page.register_link.click()

    registration_page.role_dropdown.click()

    registration_page.role_dropdown_option(2).click()

    # Then
    # Verify that error messages are hidden
    assert registration_page.type_your_name_message.is_not_visible()
    assert registration_page.you_have_to_choose_role_message.is_not_visible()
    assert registration_page.enter_your_email_message.is_not_visible()
    assert registration_page.enter_your_password_message.is_not_visible()
    assert registration_page.confirm_the_password_message.is_not_visible()

    # Verify that red validation did not kick in
    assert not registration_page.name_field.has_class('input-error')
    assert not registration_page.role_dropdown.has_class('select-error')
    assert not registration_page.email_field.has_class('input-error')
    assert not registration_page.password_field.has_class('input-error')
    assert not registration_page.confirm_password_field.has_class('input-error')

