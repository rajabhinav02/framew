import pytest
from selenium import webdriver

from testdata.testdata_home import formtestdata


def pytest_addoption(parser):
    parser.addoption("--browser_name", action = "store", default ="chrome")


@pytest.fixture(scope="class")

def setup(request):
    browsername=request.config.getoption("browser_name")

    if browsername == "chrome":
        driver= webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")

    elif browsername == "edge":
        driver = webdriver.Edge(executable_path="C:\\edgedriver_win64\\msedgedriver.exe")

    baseurl = "https://rahulshettyacademy.com/angularpractice/"
    driver.maximize_window()
    driver.get(baseurl)
    request.cls.driver = driver

    yield
    driver.quit()

#@pytest.fixture(params=formtestdata.formdata)
@pytest.fixture(params=formtestdata.testdata("TC2"))
def datavalue(request):
    return request.param

