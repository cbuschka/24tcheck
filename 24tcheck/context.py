from selenium.webdriver.support.wait import WebDriverWait


class Context:
    def __init__(self, browser, webdriver, baseUrl):
        self.baseUrl = baseUrl
        self.browser = browser
        self.webdriver = webdriver
        self.wait = WebDriverWait(browser, 5)

    # https://selenium-python.readthedocs.io/waits.html
    def waitFor(self, condition):
        self.wait.until(condition)

    def click(self, locator):
        self.browser.find_element(*locator).click()
