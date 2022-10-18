from pytest_bdd import scenarios, given, when, then

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.account_page import AccountPage
from pages.authentication_page import SignInPage
from pages.create_account_page import CreateAccountPage

scenarios('../features/test_create_account.feature')


# steps - when, then, given

@given('open the authentication page')
def load_page(browser):
    SignInPage(browser).load_page()


@when('the user types email address')
def box_email_create_account(browser):
    SignInPage(browser).box_email_create_account()


@when('the user clicks the create an account button')
def click_create_an_account_button(browser):
    SignInPage(browser).click_create_an_account_button()


@then('the user is redirected to create an account page')
def check_user_redirected_to_create_an_account_page(browser):
    WebDriverWait(browser, 5).until(ec.url_changes(SignInPage.URL))
    assert CreateAccountPage.URL == browser.current_url


@when('the user types first name')
def box_first_name(browser):
    CreateAccountPage(browser).box_first_name()


@when('the user types last name "George"')
def box_last_name(browser):
    CreateAccountPage(browser).box_last_name()


@when('the user types password "12345"')
def box_password_pozitive(browser):
    CreateAccountPage(browser).box_password_pozitive()


@when('the user types address')
def box_address(browser):
    CreateAccountPage(browser).box_address()


@when('the user types city "Tucson"')
def box_city(browser):
    CreateAccountPage(browser).box_city()


@when('the user selects state from dropdown list')
def drop_down_list_state(browser):
    CreateAccountPage(browser).drop_down_list_state()


@when('the user types zip code')
def box_zip_code(browser):
    CreateAccountPage(browser).box_zip_code()


@when('the user types mobile phone number')
def box_mobilr_phone(browser):
    CreateAccountPage(browser).box_mobilr_phone()


@when('the user clicks the register button')
def click_register_button(browser):
    CreateAccountPage(browser).click_register_button()


@then('the user is redirected to account page')
def check_user_redirected_to_account_page(browser):
    assert browser.current_url == AccountPage.URL
    print("\n---then---User is redirected to account page.")


@then('the welcome message is displayed')
def check_welcome_text_is_displayed(browser):
    account_page = AccountPage(browser)
    assert "Welcome to your account." in account_page.get_welcome_message()
    print("\n---then---Welcome message is displayed.")
