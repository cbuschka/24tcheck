from selenium import webdriver

from .context import Context
from .journeys.bounce_on_homepage import BounceOnHomepageJourney

browser = webdriver.Chrome()
try:
    ctx = Context(browser=browser, webdriver=webdriver, baseUrl="https://www.24translate.de")
    journey = BounceOnHomepageJourney(ctx=ctx)
    journey.run()
finally:
    browser.quit()
