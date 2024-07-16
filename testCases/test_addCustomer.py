import random
import string

import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("********* Test_003_AddCustomer *********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********** Login successful *****************")
        self.logger.info("************** Starting Add Customer Test ***************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCusmoterMenuItem()
        self.addcust.clickOnAddnew()

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Administrators")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Sanju")
        self.addcust.setLastName("Sri")
        self.addcust.setDob("30/07/1980")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing...........")
        self.addcust.clickOnSave()

        self.msg=self.driver.find_element(By.tag_name("body")).text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*********** Add customer test passed ************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("************ Add customer test failed **************")
            assert True == False

        self.driver.cloce()
        self.logger.info("********** Ending Test_003_AddCustomer Test ***************")

# To generate random string for email
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))
