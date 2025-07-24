import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):

        # this code will help us show where exactly we use logging
        loggerName = inspect.stack()[1][3]

        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('/Users/dogukanyavuz/PycharmProjects/PythonSelFramework/utilities/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO)
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        HomePage.getScript(self, obj=locator)
        sel.select_by_visible_text(text)
