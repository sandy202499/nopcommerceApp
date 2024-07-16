import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("************** SearchCustomerByEmail_004 **********************")
        self.driver=setup   # setup method will return the driver and we are storing that driver in this variable
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********** Login successful *****************")

        self.logger.info("*************** Starting search customer by Name ************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCusmoterMenuItem()

        self.logger.info("**************** search customer by Name ****************")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setFirstName("James")
        self.searchcust.setLasttName("Pan")
        self.searchcust.clickSearch()
        time.sleep(3)
        status=self.searchcust.searchCustomerByName("James Pan")
        assert True == status
        self.logger.info("*********************** Test_SearchCustomerByName_005 Passed and Finished")
        # assert False == status
        # self.logger.info("*********************** Test_SearchCustomerByName_005 Failed and Finished")
        self.driver.close()



