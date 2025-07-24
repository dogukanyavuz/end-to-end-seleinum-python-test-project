import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)

        # ID, XPATH, CSSSelector, Class name, Name, linkText
        homepage.getName().send_keys(getData["firstname"])
        log.info("getting the first name: "+getData["firstname"])

        homepage.getEmail().send_keys(getData["email"])  # textbox
        log.info("getting the email: "+getData["email"])

        homepage.getPassword().send_keys(getData["password"])  # textbox
        log.info("getting the password: "+getData["password"])

        homepage.getCheckbox().click()  # checkbox
        self.selectOptionByText(homepage.getDropdown(), getData["gender"])
        log.info("selecting from dropdown: "+getData["gender"])

        homepage.getSubmit().click()
        message = homepage.getMessage().text

        # homepage.getName1().send_keys(getData[0])
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
