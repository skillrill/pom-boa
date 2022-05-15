from pages.WelcomePage import WelcomePage
from pages.SigninPage import SigninPage
from utilities.ReadConfig import ReadConfig
from utilities.Logger import Logger
from time import sleep

class TestProductList:

    # class attributes
    logger = Logger.get_logger()

    # class methods = test cases
    def test_first_signin(self, setup):
        self.logger.info('********** Test Case: First Sign in')
        self.driver = setup
        self.wp = WelcomePage(self.driver)
        self.wp.click_signin_options()
        self.wp.click_first_signin()
        self.logger.info('Moving to sign in page')

        self.sp = SigninPage(self.driver)
        self.sp.signin() 
        sleep(5)
        self.logger.info('Signing in ...')
        if 'Enroll'.lower() in self.driver.page_source.lower():
            assert True
        else:
            assert False
    
