from selenium.webdriver.common.by import By

from useful.useful_elements import useful


class CreateAccountPage:
    URL = "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation"
    TITLE_TEXT = (By.CLASS_NAME, "page-heading")

    def __init__(self, browser):
        self.browser = browser

    def loadPage(self):
        self.browser.get(self.URL)

    def click_register_button(self):
        self.browser.find_element(By.CSS_SELECTOR, "#submitAccount").click()

    def gender_select(self):
        self.browser.find_element(By.ID, "id_gender1").click()

    def box_first_name(self):
        self.browser.find_element(By.CSS_SELECTOR, "#customer_firstname").send_keys(useful.random_firstname_gen)

    def box_last_name(self):
        self.browser.find_element(By.CSS_SELECTOR, "#customer_lastname").send_keys(useful.LastName)

    def box_email(self):
        self.browser.find_element(By.CSS_SELECTOR, "#email").send_keys(useful.random_mail_gen)

    def box_password_pozitive(self):
        self.browser.find_element(By.CSS_SELECTOR, "#passwd").send_keys(useful.Password_Pozitive)

    def box_password_negative(self):
        self.browser.find_element(By.CSS_SELECTOR, "#passwd").send_keys(useful.Password_Negative)

    def box_address(self):
        self.browser.find_element(By.CSS_SELECTOR, "#address1").send_keys(useful.random_address_gen)

    def box_city(self):
        self.browser.find_element(By.CSS_SELECTOR, "#city").send_keys("Tucson")

    def drop_down_list_state(self):
        self.browser.find_element(By.CSS_SELECTOR, "#id_state > option:nth-child(4)").click()

    def box_zip_code(self):
        self.browser.find_element(By.CSS_SELECTOR, "#postcode").send_keys(useful.random_zip_gen)

    def box_mobilr_phone(self):
        self.browser.find_element(By.CSS_SELECTOR, "#phone_mobile").send_keys(useful.random_phone_gen)
