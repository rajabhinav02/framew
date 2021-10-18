from selenium.webdriver.common.by import By

from pages.brands import brandpage


class homepage:

    def __init__(self, driver):
        self.driver= driver

    namelocation = (By.XPATH,"//input[@name='name']")
    emaillocation = (By.CSS_SELECTOR,"[name='email']")
    passwordlocation = (By.CSS_SELECTOR,"#exampleInputPassword1")
    icecheckboxlocation = (By.ID,"exampleCheck1")
    genderlocation = (By.ID, "exampleFormControlSelect1")
    empstatus = (By.XPATH, "//input[@type='radio']")
    datelocation = (By.CSS_SELECTOR, "[name='bday']")
    submitlocation = "[type='submit']"
    shoplocation = (By.LINK_TEXT, "Shop")
    successlocation = (By.XPATH, "//div[contains (@class, 'alert-success')]")
    homelocation = (By.LINK_TEXT, "Home")


    def getname(self):
        return self.driver.find_element(*homepage.namelocation)

    def getemail(self):
        return self.driver.find_element(*homepage.emaillocation)

    def getpwd(self):
        return self.driver.find_element(*homepage.passwordlocation)

    def geticecream(self):
        return self.driver.find_element(*homepage.icecheckboxlocation)

    def getgender(self):
        return self.driver.find_element(*homepage.genderlocation)

    def getempstatuses(self):
        return self.driver.find_elements(*homepage.empstatus)

    def getdate(self):
        return self.driver.find_element(*homepage.datelocation)

    def getsubmitlocation(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.submitlocation)

    def getshop(self):
        self.driver.find_element(*homepage.shoplocation).click()
        brand = brandpage(self.driver)
        return brand

    def getHome(self):
        self.driver.find_element(*homepage.homelocation)

    def clickhome(self):
        self.getHome().click()

    def getsuccess(self):
        return self.driver.find_element(*homepage.successlocation)

    def clicksubmit(self):
        self.getsubmitlocation().click()
