from selenium.webdriver.common.by import By


class confirmpage:

    def __init__(self, driver):
        self.driver = driver

    countrylocation = (By.CSS_SELECTOR, "#country")
    displayedcountrylocation = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    purchasebuttonlocation = (By.XPATH, "//input[contains (@class, 'btn-success') and (@type='submit')]")
    finalsuccessmsglocation = (By.XPATH, "//strong")

    
    def getcountrylocation(self):
        return self.driver.find_element(*confirmpage.countrylocation)

    def getallcountries(self):
        return self.driver.find_elements(*confirmpage.displayedcountrylocation)

    def getpurchasebutton(self):
        return self.driver.find_element(*confirmpage.purchasebuttonlocation)

    def getfinalsuccess(self):
        suc= self.driver.find_element(*confirmpage.finalsuccessmsglocation).text

        if "Success" in suc:
            return True
        else:
            return False




