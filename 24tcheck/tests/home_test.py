from ..journeys.visit_home_journey import VisitHomeJourney
from ..ui_test_base import UiTestBase


class HomeTest(UiTestBase):

    def test_home_page_available(self):
        journey = VisitHomeJourney(ctx=self.seleniumContext)
        journey.run()
