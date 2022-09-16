from pytest_bdd import scenarios, given, when, then, parsers

# scenarios
from selenium.webdriver.common.by import By

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
    assert browser.current_url == AccountPage.URL
    print("\n---then---User is redirected to account page.")


@then('the user is on the alert signin page')
def check_user_stays_on_sign_in_page(browser):
    sign_in_page = SignInPage(browser)
    assert browser.current_url == sign_in_page.ALERT_SIGNIN_PAGE
    print("\n---then---User is on the alert signin page.")


@then(parsers.cfparse('"{alert}" error message is displayed'))
def check_alert_message(browser, alert):
    sign_in_page = SignInPage(browser)
    string = browser.find_element(By.CSS_SELECTOR, "ol:nth-child(2) > li:nth-child(1)").text
    assert alert == browser.find_element(By.CSS_SELECTOR, "ol:nth-child(2) > li:nth-child(1)").text
    print(f"\n---then---Error message is displayed: {string}\n")


@then('the welcome message is displayed')
def check_welcome_text_is_displayed(browser):
    account_page = AccountPage(browser)
    assert "Welcome to your account." in account_page.get_welcome_message()
    print("\n---then---Welcome message is displayed.")


@then('the signout button is displayed')
def check_sign_out_button_is_displayed(browser):
    # account_page = AccountPage(browser)
    assert browser.find_element(By.CSS_SELECTOR, ".logout")
    print("\n---then---Signout button is displayed.")
