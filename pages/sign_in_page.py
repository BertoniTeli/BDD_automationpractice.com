from selenium.webdriver.common.by import By

from useful.useful_elements import useful, SignIn


class SignInPage:
    # LOCATORS:
    URL = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    ALERT_SIGNIN_PAGE = "http://automationpractice.com/index.php?controller=authentication"
    TITLE_TEXT = (By.CSS_SELECTOR, "h1")
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR, "#SubmitCreate")
    BUTTON_SIGN_IN = (By.CSS_SELECTOR, "#SubmitLogin")

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def box_email_create_account(self):
        self.browser.find_element(By.ID, "email_create").send_keys(useful.Random_Email_Gen)

    def box_email_sign_in(self, username):
        self.browser.find_element(By.CSS_SELECTOR, "#email").send_keys(username)

    def box_password_sign_in(self, password):
        self.browser.find_element(By.CSS_SELECTOR, "#passwd").send_keys(password)

    def click_sign_in(self):
        self.browser.find_element(*self.BUTTON_SIGN_IN).click()

    def get_alert_message(self):
        self.browser.find_element(By.CSS_SELECTOR, "#center_column > div:nth-child(2)")
