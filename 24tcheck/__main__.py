from selenium import webdriver

from .context import Context
from .journeys.bounce_on_homepage import BounceOnHomepageJourney

browser = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                           desired_capabilities={
                               "browserName": "chrome",
                               "platform": "Linux"
                           })
# browser = webdriver.Chrome()
browser.fullscreen_window()
try:
    ctx = Context(browser=browser, webdriver=webdriver, baseUrl="https://www.24translate.de")
    journey = BounceOnHomepageJourney(ctx=ctx)
    journey.run()
finally:
    browser.quit()
