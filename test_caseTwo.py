import pytest
from Pages.SearchPage import Launchpage
from Base_Driver.BaseClass import Baseclass
import pytest_html
from Utilities.Utils import Utils
import time


class Test_ProductByStarFilter(Baseclass):
      log = Utils.custom_logger()
      @pytest.fixture(autouse=True)
      def class_setup(self):

          self.sp = Launchpage(self.browser, self.wait)

      @pytest.mark.smoke
      def test_AddToCartFunctionality(self):

          self.browser.get('https://www.amazon.in/Himalayan-Organics-Organic-Vitamin-B12/dp/B07Y7P2S5T/ref=sr_1_1?crid=X4JYY1XROLDZ&dib=eyJ2IjoiMSJ9.mYofFxkbLTHEoPpGqU45DApoRvoo2MXFry3hmgIuSH1ZPlWCddTXLv60SWI6X6XVYfG0G5Atewt5GrlAjEQAm4JiJRhpBwpMp2MuKeffqoJ1z-uiJ8o0IHwa8FqvqGE4tFskkBdbf7Sn2iIFUgOcn9ay7uNfqYv8tQNPBPXO_fxFcg4nM-16qbEWpgW6BhYLLjvzgeVTn4DFzYUMojjx4RRmoY2tAGsMLMo8o9JBBxnN6WxdDqFHW-hM5q-lEbt45I9JWCko-MnKYG0RcU5QVLUzjsQDiJZQXUyGQltpEWk.CHjFA5bkfonv_hK5L6f_jSAoc4gxEm7jUcdqwu05mq4&dib_tag=se&keywords=b12+supplement&qid=1709793945&refinements=p_72%3A1318476031&rnid=1318475031&sprefix=%2Caps%2C198&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1')
          ProductPrice =self.sp.GetProductPrice()
          #print(ProductPrice)
          self.sp.SelectQty()
          self.sp.ClickAddToCArtButton()
          Cartqty = self.sp.GetCartQty()
          #print(Cartqty)
          total_price = self.sp.GetTotalPrice()
          assert int(total_price) == int(ProductPrice) * int(Cartqty)
          self.log.info("add to cart functionality verified")



