import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import requests

response = requests.get('https://rahulshettyacademy.com/angularpractice/')
print(response)  # printed the get request

assert response.status_code == 200  # If response is 200, we can move forward with the project

s = Service('../path/chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# XPATH = //a[contains(@href,'shop')]
# CSS_SELECTOR = a[href*='shop']

driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()  # new XPATH usage

productList = driver.find_elements(By.XPATH, "//app-card[contains(@class,'mb-3')]")
for products in productList:
    elementText = products.find_element(By.XPATH, "div/div/h4/a").text  # chained with 20th line
    if elementText == "Blackberry":
        products.find_element(By.XPATH, "div/div/button").click()  # chained with 20th line
        break

driver.find_element(By.XPATH, "//a[contains(@class,'btn')]").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("tu")

wait = WebDriverWait(driver, 10)
wait.until(
    expected_conditions.presence_of_element_located((By.LINK_TEXT, "Turkey"))
)

driver.find_element(By.LINK_TEXT, "Turkey").click()
driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.CLASS_NAME, "btn-lg").click()
successText = driver.find_element(By.XPATH, "//div[contains(@class,'alert')]").text

assert "Success! Thank you!" in successText

print(successText)
driver.close()