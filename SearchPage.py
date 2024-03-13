from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
from Utilities.Utils import Utils
from Base_Driver.Base_Driver import Baseclass
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import time
class Launchpage(Baseclass):
      log = Utils.custom_logger(logLevel=logging.INFO)

      SearchTextBox = '//*[@id="twotabsearchtextbox"]'
      SubmitButton = '//*[@id="nav-search-submit-button"]'
      Filter_fourStar = '//*[@id="p_72/1318476031"]/span/a'
      list_of_Results = '//*[@id="search"]/span[2]/div/h1/div/div[1]/div/div/span[1]'
      PageResults = '//div[@class = "sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"]'
      NextPageButton =  '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[67]/div/div/span/a[1]'
      QtyDropdown = '//*[@id="quantity"]'
      ProductPrice = '//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]'
      AddToCartButton = '//*[@id="add-to-cart-button"]'
      GoToCart = '//*[@id="sw-gtc"]/span/a'
      CartQty = "//span[@class = 'sc-action-quantity']"
      TotalAmount = "//span[@id = 'sc-subtotal-amount-activecart']/span"
      AccountList  = '//*[@id="nav-link-accountList"]'
      SignInButton = '//*[@id="nav-flyout-ya-signin"]/a/span'

      def __init__(self,browser,wait):
          super().__init__(browser,wait)


      def SearchProduct(self,ProductName):
          time.sleep(2)
          self.browser.find_element(By.XPATH, self.SearchTextBox).send_keys(ProductName)
          time.sleep(4)
          self.browser.find_element(By.XPATH,self.SubmitButton).click()
          time.sleep(6)

      def FilterProduct_4StarReviews(self):
          self.browser.find_element(By.XPATH, '//*[@id="p_72/1318476031"]/span/a').click()
          time.sleep(4)
          No_of_Results = self.browser.find_element(By.XPATH, '//*[@id="search"]/span[2]/div/h1/div/div[1]/div/div/span[1]').text

          return No_of_Results

      def GetPageResults(self):
          pageResults = self.browser.find_elements(By.XPATH, self.PageResults)
          pageResults = len(pageResults)
          return pageResults

      def ClickNextPage(self):
          self.browser.find_element(By.XPATH, self.NextPageButton).click()

      def GetProductPrice(self):
          ProductPrice = self.wait_until_element_is_clickable(By.XPATH,self.ProductPrice).text
          ProductPrice = list(ProductPrice)
          ProductPrice = ''.join(ProductPrice[1:])
          print(ProductPrice)
          return ProductPrice



      def SelectQty(self):
          self.browser.execute_script("window.scrollBy(0,500);")
          select = Select(self.browser.find_element(By.XPATH, self.QtyDropdown))
          select.select_by_value('2')

      def ClickAddToCArtButton(self):
          self.wait_until_element_is_clickable(By.XPATH, self.AddToCartButton).click()
          self.wait_until_element_is_clickable(By.XPATH, self.GoToCart).click()
          time.sleep(2)

      def GetCartQty(self):
          Cartqty = self.browser.find_element(By.XPATH, self.CartQty).text
          Cartqty = Cartqty.split()
          Cartqty = (Cartqty[13])
          Cartqty = Cartqty.split(':')
          Cartqty = (int(Cartqty[1]))
          return Cartqty

      def GetTotalPrice(self):
          total_price = self.browser.find_element(By.XPATH, self.TotalAmount).text
          total_price = ''.join(total_price.split())
          total_price = total_price.replace(',', '')
          total_price = total_price.replace('.00', '')
          return total_price

      def ClickOnOrders(self):
          action = ActionChains(self.browser)
          AccountListLink = self.browser.find_element(By.XPATH,self.AccountList)
          action.move_to_element(AccountListLink)
          time.sleep(2)
          SignInLink = self.browser.find_element(By.XPATH, self.SignInButton)
          action.move_to_element(SignInLink).click().perform()












