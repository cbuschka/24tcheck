import unittest

from selenium import webdriver

from .context import Context


class UiTestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                       desired_capabilities={
                                           "browserName": "chrome",
                                           "platform": "Linux"
                                       })
        # browser = webdriver.Chrome()
        cls.browser.fullscreen_window()

    def setUp(self):
        self.seleniumContext = Context(browser=self.browser, baseUrl="https://www.24translate.de")

    def tearDown(self):
        self.seleniumContext.close()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
