from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        """

        :rtype: object
        """
        self.driver = driver

    countryTextbox = (By.ID, "country")
    turkeyText = (By.LINK_TEXT, "Turkey")
    checkbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
    purchaseButton = (By.CLASS_NAME, "btn-lg")
    successText = (By.XPATH, "//div[contains(@class,'alert')]")

    def getCountryTextbox(self):
        return self.driver.find_element(*ConfirmPage.countryTextbox)

    def getTurkey(self):
        return self.driver.find_element(*ConfirmPage.turkeyText)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getSuccessText(self):
        return self.driver.find_element(*ConfirmPage.successText)
