from selenium.webdriver.common.by import By

from pages.checkout import checkoutpage


class brandpage:

    def __init__(self, driver):
        self.driver = driver

    addbuttonslocation = (By.XPATH, "//button[contains(@class, 'btn-info')]")
    checkoutlocation = (By.CSS_SELECTOR, "[class*='nav-link btn']")

    def getaddbuttons(self):
        return self.driver.find_elements(*brandpage.addbuttonslocation)

    def getcheckout(self):
        self.driver.find_element(*brandpage.checkoutlocation).click()
        check = checkoutpage(self.driver)
        return check



