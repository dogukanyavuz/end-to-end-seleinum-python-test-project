from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(@href,'shop')]")  # tuple
    productList = (By.XPATH, "//app-card[contains(@class,'mb-3')]")
    name = (By.XPATH, "//div/input[@name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, "alert-success")
    name1 = (By.XPATH, "//h4/input[@type='text']")

    # return self.driver.find_element(*HomePage.shop)
    # class variables should be called with "classname.variableName"
    # instance variable should be called with "self.variableName"
    # we have to use '*' operator in order shop variable to be 2 arguments, key and value
    # if we don't use '*' operator, (By.XPATH, "//a[contains(@href,'shop')]") this tuple is considered 1 argument
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    def getProductText(self, obj):
        chainedLocator = "div/div/h4/a"
        return obj.find_element(By.XPATH, chainedLocator).text

    def getProductButton(self, obj):
        chainedLocator1 = "div/div/button"
        return obj.find_element(By.XPATH, chainedLocator1)

    def getProductList(self):
        return self.driver.find_elements(*HomePage.productList)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getDropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getScript(self, obj):
        return self.driver.execute_script("arguments[0].scrollIntoView();", obj)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message)

    def getName1(self):
        return self.driver.find_element(*HomePage.name1)
