import pytest

from pages.homepage import homepage
from utility.base import baseclass


class TestShop(baseclass):

    @pytest.fixture(autouse=True)
    def classsetup(self):
        self.home = homepage(self.driver)
        self.log = self.logg()


    def test_form(self, datavalue):
        #log = self.logg()
        #home = homepage(self.driver)

        self.home.getname().send_keys(datavalue["firstname"])
        self.home.getemail().send_keys(datavalue["email"])
        self.home.getpwd().send_keys(datavalue["pwd"])
        self.home.geticecream().click()
        self.dropdown(self.home.getgender(), "Female")
        empstatus = self.home.getempstatuses()
        for radio in empstatus:
            if radio.get_attribute('value') == 'option1':
                radio.click()

        assert not empstatus[2].is_enabled()

        self.home.getdate().click()
        self.home.getdate().send_keys("14")
        self.home.getdate().send_keys("06")
        self.home.getdate().send_keys("2021")

        self.home.clicksubmit()
        self.logg().info("Form entry completed")
        assert "Success" in self.home.getsuccess().text

        self.driver.refresh()

    def test_shoping(self):

        self.brand = self.home.getshop()

        addbuttonslocation = self.brand.getaddbuttons()

        for add in addbuttonslocation:
            brandname = add.find_element_by_xpath("parent::div/parent::div//h4").text
            if brandname == 'Blackberry':
                add.click()
        self.check = self.brand.getcheckout()

        brandname2 = self.check.getbrandnames().text
        self.logg().info("Brand name selected is " + brandname2)
        quantityselected = self.check.getquantity().text
        self.logg().info("Quantity selected is " + quantityselected)
        price = self.check.getprice().text
        self.logg().info("Price is " + price[3:])
        totalamount = self.check.getfirsttotal().text
        self.logg().info("First total is " + totalamount[3:])
        finaltotal = self.check.getfinaltotal().text
        self.logg().info("Final total is " + finaltotal[3:])

        assert brandname2 == brandname
        # assert quantityselected*int(price[3:]) == int(totalamount[3:])
        assert 1 * int(price[3:]) == int(totalamount[3:])

        self.confirmation = self.check.clickcheckout()

        self.confirmation.getcountrylocation().send_keys("I")
        self.waitxpath(self.confirmation.displayedcountrylocation, 15)

        displayedcountrylocation = self.confirmation.getallcountries()

        for country in displayedcountrylocation:
            if country.text == "India":
                country.click()
                break

        self.confirmation.getpurchasebutton().click()
        result = self.confirmation.getfinalsuccess()
        assert result == True
        #self.driver.back()
        #self.driver.refresh()











