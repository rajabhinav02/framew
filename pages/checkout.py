from selenium.webdriver.common.by import By

from pages.confirm import confirmpage


class checkoutpage:

    def __init__(self, driver):
        self.driver = driver

    brandnameselected = (By.XPATH, "//h4[@class='media-heading']/a")
    quantity = (By.CSS_SELECTOR, "#exampleInputEmail1")
    pricelocation = (By.XPATH, "//table[contains (@class, 'table')]//tr/td[3]/strong")
    totalamountlocation = (By.XPATH, "//table[contains (@class, 'table')]//tr/td[4]/strong")
    finaltotallocation = (By.XPATH, "//table[contains(@class, 'table-hover')]//tr[2]/td[5]//strong")
    finalcheckoutlocation = (By.XPATH, "//button[contains(@class, 'btn-success')]")

    def getbrandnames(self):
        return self.driver.find_element(*checkoutpage.brandnameselected)

    def getquantity(self):
        return self.driver.find_element(*checkoutpage.quantity)

    def getprice(self):
        return self.driver.find_element(*checkoutpage.pricelocation)

    def getfirsttotal(self):
        return self.driver.find_element(*checkoutpage.totalamountlocation)

    def getfinaltotal(self):
        return self.driver.find_element(*checkoutpage.finaltotallocation)

    def getcheckout(self):
        return self.driver.find_element(*checkoutpage.finalcheckoutlocation)

    def clickcheckout(self):
        self.getcheckout().click()
        confirmation = confirmpage(self.driver)
        return confirmation


