import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

EDGE_DRIVER_PATH = "/Users/dogukanyavuz/Downloads/edgedriver_mac64/msedgedriver"
# Edge Dev uygulamasının gerçek binary yolu:
EDGE_BINARY_PATH = (
    "/Applications/Microsoft Edge Dev.app/Contents/MacOS/Microsoft Edge Dev"
)

response = requests.get("https://rahulshettyacademy.com/angularpractice/")
assert response.status_code == 200

service = Service(EDGE_DRIVER_PATH)
options = Options()
options.binary_location = EDGE_BINARY_PATH
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()

product_list = driver.find_elements(By.XPATH, "//app-card[contains(@class,'mb-3')]")
for product in product_list:
    element_text = product.find_element(By.XPATH, "div/div/h4/a").text
    if element_text == "Blackberry":
        product.find_element(By.XPATH, "div/div/button").click()
        break

driver.find_element(By.XPATH, "//a[contains(@class,'btn')]").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("tu")
wait = WebDriverWait(driver, 10)
# By.LINK_TEXT sadece <a> etiketlerinin text içeriğine bakar.
# Yani burada "Turkey" yazan linki arar, xpath değil.
# Bu satır explicit wait: Turkey linki DOM'da çıkana kadar en fazla 10 saniye bekle.
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Turkey")))

# Burada element zaten DOM'da olduğu için click() ile tıklıyoruz.
# Bu satır bekleme yapmaz; sadece bulduğu linke tıklar.
driver.find_element(By.LINK_TEXT, "Turkey").click()
driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
driver.find_element(By.CLASS_NAME, "btn-lg").click()

success_text = driver.find_element(By.XPATH, "//div[contains(@class,'alert')]").text
print("Success text:", success_text)

time.sleep(2)
driver.quit()
