from selenium.webdriver.common.by import By

class SigninPage:

    # class attributes
    textbox_username_css = '#username'
    textbox_passcode_css = '#passcode'
    button_signin_xpath = "//a[text()='Sign In']"

    # class constructor, initializer
    def __init__(self, driver):
        self.driver = driver
    
    # class method, actions, behavior
    def signin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_css).click()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_passcode_css).click()
        self.driver.find_element(By.XPATH, self.button_signin_xpath).click()