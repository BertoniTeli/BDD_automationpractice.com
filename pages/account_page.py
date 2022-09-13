from selenium.webdriver.common.by import By

class AccountPage:
    URL = "http://automationpractice.com/index.php?controller=my-account"
    WELCOME_TEXT = (By.CSS_SELECTOR, ".info-account")
    SIGN_OUT_BUTTON = (By.CSS_SELECTOR, ".logout")

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_current_url(self):
        return self.browser.current_url

    def get_welcome_message(self):
        # daca merge......???
        return self.browser.find_element(*self.WELCOME_TEXT).text

    def click_signout_button(self):
        self.browser.find_element(*self.SIGN_OUT_BUTTON).click()
