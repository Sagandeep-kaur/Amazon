import pytest
from Pages.SearchPage import Launchpage
from Base_Driver.BaseClass import Baseclass
from Utilities.Utils import Utils
import pytest_html
import time


class Test_ProductByStarFilter(Baseclass):
      log = Utils.custom_logger()
      @pytest.fixture(autouse=True)
      def class_setup(self):

          self.sp = Launchpage(self.browser, self.wait)

      def test_ProductStarFilter(self):
          self.sp.SearchProduct('B12 Supplement')
          No_of_Results_On_Screen = self.sp.FilterProduct_4StarReviews()
          print(No_of_Results_On_Screen)
          No_of_Results_On_Screen = No_of_Results_On_Screen.split()

          No_of_Results_On_Screen = No_of_Results_On_Screen[2]
          print(No_of_Results_On_Screen)
          PageOneResults = self.sp.GetPageResults()
          print(PageOneResults)
          self.sp.ClickNextPage()
          time.sleep(5)
          PageTwoResults = self.sp.GetPageResults()
          print(PageOneResults)
          assert int(No_of_Results_On_Screen) == PageOneResults + PageTwoResults
          self.log.info("No_of_Results_On_Screen verified")
          time.sleep(5)

      @pytest.mark.skip
      def test_SignInLink(self):
          self.sp.ClickOnOrders()
          assert self.browser.title == 'Amazon Sign In'
          self.log.info("Sign in Link verified")
