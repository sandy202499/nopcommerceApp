import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFisrtName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchResults_xpath = "//table[@class='table table-bordered table-hover table-striped dataTable no-footer']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFisrtName_id).clear()
        self.driver.find_element(By.ID, self.txtFisrtName_id).send_keys(fname)

    def setLasttName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    # def getNoOfRows(self):
    #     return len(self.driver.find_element(By.XPATH, self.tableRows_xpath))
    def getNoOfRows(self):
        rows = self.driver.find_elements(By.XPATH, self.tableRows_xpath)
        return len(rows)

    def getNoOfColumns(self):
        return len(self.driver.find_element(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH, self.table_xpath)
            emailid=table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name=table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag





