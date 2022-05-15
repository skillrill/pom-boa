from utilities.Logger import Logger

class TestWelcomePage:

    # class attributes
    logger = Logger.get_logger()

    # class methods = test cases
    def test_welcome_page_title(self, setup):
        self.driver = setup
        page_title = self.driver.title
        self.logger.info('********** Test Case: Validating Welcome Page Title ')
        if 'Welcome' in page_title:
            assert True
        else:
            assert False