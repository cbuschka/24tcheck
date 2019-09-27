from ..model.home_page import HomePage


class VisitHomeJourney:
    def __init__(self, ctx):
        self.ctx = ctx

    def run(self):
        homePage = HomePage(self.ctx)
        homePage.open()
        homePage.waitForPresent()
        homePage.waitForOrderTranslationLinkPresent()
