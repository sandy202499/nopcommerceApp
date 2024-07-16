import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()



    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********** Test_001_Login ************")
        self.logger.info("****************** Verifying Home Page Title ****************** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")   # For screenshots we need to add only this line, no other code needed
            assert True
            self.driver.close()
            self.logger.info(" ************** Home Page title test is passed ***************** ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")     #Name of the screenshot will be same name as test case methos
            self.driver.close()
            self.logger.error(" ************** Home Page title test is failed ***************** ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info(" ************** Verifying Login test ***************** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            assert True
            self.logger.info(" ************** Login test is passed ***************** ")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")    #Name of the screenshot will be same name as test case methos
            self.driver.close()
            self.logger.error(" ************** Login test is failed ***************** ")
            assert False
