from selenium.webdriver.common.by import By
from utilities.ReadConfig import ReadConfig

class WelcomePage:

    # class attributes
    # valid_username = ReadConfig.get_valid_username()
    # valid_password = ReadConfig.get_valid_password()
    button_signin_options_css = '#landing_sign'
    button_first_signin_css = "[aria-labelledby='signInOpt1']"

    # class constructor, initializer
    def __init__(self, driver):
        self.driver = driver
    
    # class method, actions, behavior
    def click_signin_options(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_signin_options_css).click()
    
    def click_first_signin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_first_signin_css).click()