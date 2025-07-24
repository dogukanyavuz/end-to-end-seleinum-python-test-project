import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
# instead of using pytest, we created BaseClass and gave it the knowledge of fixture
# BaseClass now has the knowledge of fixture, that's why we can remove it from here and just inherit it


class TestOne(BaseClass):

    def test_e2e(self):

        # XPATH = //a[contains(@href,'shop')]
        # CSS_SELECTOR = a[href*='shop']

        log = self.getLogger()
        homePage = HomePage(self.driver)

        # self.driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()  # new XPATH usage
        # instead of typing the code above, we can type the code below
        # we used a smart way to create checkoutPageObject
        # clicking on the element and creating an object for next class is inside "shopItems()"
        checkoutPageObject = homePage.shopItems()

        #product_list = self.driver.find_elements(By.XPATH, "//app-card[contains(@class,'mb-3')]")
        product_list = homePage.getProductList()
        #checkoutPage = CheckoutPage(self.driver)

        for products in product_list:
            #element_text = products.find_element(By.XPATH, "div/div/h4/a").text  # chained with 33'th line
            element_text = homePage.getProductText(products)
            log.info(element_text)
            if element_text == "Blackberry":
                #products.find_element(By.XPATH, "div/div/button").click()  # chained with 33'th line
                log.info(element_text)
                homePage.getProductButton(products).click()
                break

        checkoutPageObject.getCheckoutButton().click()

        # I handled creating object and clicking on the checkout button inside getSecondCheckoutButton()
        confirmPage = checkoutPageObject.getSecondCheckoutButton()

        confirmPage.getCountryTextbox().send_keys("tu")
        self.verifyLinkPresence("Turkey")
        log.info("explicit wait, method is in BaseClass")

        confirmPage.getTurkey().click()
        confirmPage.getCheckbox().click()
        confirmPage.getPurchaseButton().click()
        success_text = confirmPage.getSuccessText().text

        assert "Success! Thank you!" in success_text
