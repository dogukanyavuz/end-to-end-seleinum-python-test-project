from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//app-card[contains(@class,'mb-3')]")
    checkoutButton = (By.XPATH, "//a[contains(@class,'btn')]")
    secondCheckoutButton = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_element(*CheckoutPage.cardTitle)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def getSecondCheckoutButton(self):
        self.driver.find_element(*CheckoutPage.secondCheckoutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
