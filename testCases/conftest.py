import pytest
from selenium import webdriver


# Repeated steps/common things in test cases (test_login) will be included here
#self.driver = webdriver.Chrome()
#self.driver.get(self.baseURL)


@pytest.fixture
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        driver.maximize_window()
        print("Launching Chrome browser .............")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        driver.maximize_window()
        print("Launching Firefox browser ............")
    else:
        driver=webdriver.Edge()
        driver.maximize_window()
        print("Launching Edge browser ............")
    return driver

# To run the test in desired browser
def pytest_addoption(parser):         # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                # This will return the browser value to setup method
    return request.config.getoption("--browser")

###########  To generate pytest HTML Report  #################

# It is hook for adding  Environment info to HTML report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Sanju'


def pytest_configure(config):
    config._metadata = {
        'Project Name': 'nop commerce',
        'Module Name': 'Customers',
        'Tester': 'Sanju'
         }


#It is hook for Delete/Modify Environment info to HTML report
@pytest.mark.Optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_metadata(metadata):
#     metadata.pop("Plugins", None)
#     metadata.pop("Platform", None)