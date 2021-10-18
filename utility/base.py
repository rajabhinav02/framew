import inspect
import logging
import time

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class baseclass:



    def dropdown(self, locator, value):
        select = Select(locator)
        select.select_by_visible_text(value)

    def logg(self):
        tcname =inspect.stack()[1][3]
        logger=logging.getLogger(tcname)
        fileloc = logging.FileHandler("logge.log")
        format = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileloc.setFormatter(format)
        logger.addHandler(fileloc)
        logger.setLevel(logging.DEBUG)
        return logger

    def waitxpath(self, locator, time):
        wait= WebDriverWait(self.driver, time)
        wait.until(expected_conditions.presence_of_element_located(locator))

    
