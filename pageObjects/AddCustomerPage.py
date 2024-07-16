import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


class AddCustomer():
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"

    txtcustomerRoles_xpath = "//select[@id='SelectedCustomerRoleIds']"
    lstitemAdministered_xpath = "//option[normalize-space()='Administrators']"
    lstitemForumModerators_xpath= "//option[normalize-space()='Forum Moderators']"
    lstitemRegistered_xpath = "//option[@value='3']"
    lstitemGuests_xpath = "//option[@value='4']"
    lstitemVendor_xpath = "//option[@value='5']"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"

    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()
        #self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()
        time.sleep(3)

    def clickOnCusmoterMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)
        time.sleep(3)
# ************************************************************************************
    # def setCustomerRoles(self, role):
    #     self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
    #     time.sleep(3)
    #     if role == 'Registered':
    #         self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
    #     elif role == 'Administrators':
    #         self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministered_xpath)
    #     elif role == 'Guests':
    #         time.sleep(3)
    #         # #self.driver.find_element(By.XPATH, "//li[@title='Registered']//span[@role='presentation'][normalize-space()='×']").click()
    #         # #self.driver.find_element(By.XPATH, "//span[@role='presentation']").click()
    #         # #self.driver.find_element(By.XPATH, "//option[@value='3']")
    #         # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.XPATH, "//option[@value='3']")).click()
    #         self.driver.find_element(By.XPATH, "//*[@class = 'select2-selection__choice__remove']").click()
    #         self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
    #     elif role == 'Vendors':
    #         self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendor_xpath)
    #     else:
    #         self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
    #     time.sleep(3)
    #     #self.listitem.click()
    #     self.driver.execute_script("arguments[0].click();", self.listitem)

# ***************************************************************************

    def setCustomerRoles(self, role):
        # Click to open the customer roles selection
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txtcustomerRoles_xpath))
        ).click()
        time.sleep(3)

        # Remove Registered role if it's present
        if role != 'Registered':
            try:
                registered_role_remove_button = self.driver.find_element(By.XPATH,
                                                                         "//li[@title='Registered']//span[@role='presentation']")
                self.driver.execute_script("arguments[0].click();", registered_role_remove_button)
            except NoSuchElementException:
                pass  # If the Registered role is not present, continue

        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministered_xpath)
        elif role == 'Guests':
            try:
                guests_role_remove_button = self.driver.find_element(By.XPATH,
                                                                     "//li[@title='Guests']//span[@role='presentation']")
                self.driver.execute_script("arguments[0].click();", guests_role_remove_button)
            except NoSuchElementException:
                pass  # If the Guests role is not present, continue
            self.listitem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.lstitemGuests_xpath))
            )
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendor_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)

        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.listitem)
        try:
            self.driver.execute_script("arguments[0].click();", self.listitem)
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", self.listitem)


# *******************************************************************

    def setManagerOfVendor(self, value):
        drp=Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text()

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH, self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_leys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()




