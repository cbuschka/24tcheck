from ..journeys.bounce_on_homepage import BounceOnHomepageJourney
from ..ui_test_base import UiTestBase


class HomeTest(UiTestBase):

    def test_home_page_available(self):
        journey = BounceOnHomepageJourney(ctx=self.seleniumContext)
        journey.run()
