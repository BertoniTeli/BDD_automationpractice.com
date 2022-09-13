from selenium.webdriver.common.by import By


class main_page_elements:
    URL = "http://automationpractice.com/index.php"
    SIGNIN_BUTTON = (By.CSS_SELECTOR, "[class='login']")
    WOMAN_BUTTON = (By.CSS_SELECTOR, "li > [title='Women']")

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_signin_button(self):
        self.browser.find_element(*self.SIGNIN_BUTTON).click()
