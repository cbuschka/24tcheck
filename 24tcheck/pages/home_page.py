from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, ctx):
        self.ctx = ctx

    def open(self):
        self.ctx.browser.get(self.ctx.baseUrl + "/")

    def waitForPresent(self):
        self.ctx.waitFor(EC.title_contains("Übersetzungsbüro 24translate"))

    def waitForOrderTranslationLinkPresent(self):
        self.ctx.waitFor(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/uebersetzungsangebot.html']")))

    def clickOrderTranslation(self):
        self.ctx.click((By.CSS_SELECTOR, "a[href*='/uebersetzungsangebot.html']"))
