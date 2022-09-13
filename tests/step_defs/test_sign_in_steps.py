import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# scenarios

from pages.sign_in_page import SignInPage
from pages.account_page import AccountPage

scenarios('../features/test_sign_in.feature')


# steps - when, then, given

@given('open the login page')
def load_page(browser):
    sign_in_page = SignInPage(browser)
    sign_in_page.load_page()


@when(parsers.cfparse('the user types username "{username}"'))
@when('the user types username "<username>"')
def box_email_sign_in(browser, username):
    sign_in_page = SignInPage(browser)
    sign_in_page.box_email_sign_in(username)


@when(parsers.cfparse('the user types password "{password}"'))
@when('the user types password "<password>"')
def box_password_sign_in(browser, password):
    sign_in_page = SignInPage(browser)
    sign_in_page.box_password_sign_in(password)


@when('the user clicks the signin button')
def click_sign_in(browser):
    sign_in_page = SignInPage(browser)
    sign_in_page.click_sign_in()


@then('the user is redirected to account page')
def check_user_redirected_to_account_page(browser):
    account_page = AccountPage(browser)
    assert browser.current_url == account_page.URL


@then('the user is on the login page')
def check_user_stays_on_sign_in_page(browser):
    sign_in_page = SignInPage(browser)
    assert browser.current_url == sign_in_page.URL


@then('"<alert>" error message is displayed')
def check_alert_message(browser):
    sign_in_page = SignInPage(browser)
    assert "<alert>" == sign_in_page.get_alert_message()


@then('the welcome message is displayed')
def check_welcome_text_is_displayed(browser):
    account_page = AccountPage(browser)
    assert "Welcome to your account." in account_page.get_welcome_message()


@then('the signout button is displayed')
def check_sign_out_button_is_displayed(browser):
    account_page = AccountPage(browser)
    assert "#SubmitLogin" in browser.current_url
