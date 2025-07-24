import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Safari()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()  # maximizes the page

# ID, XPATH, CSSSelector, Class name, Name, linkText
driver.find_element(By.XPATH, "//div/input[@name='name']").send_keys("Dogukan")
driver.find_element(By.NAME, "email").send_keys("dogukan.yavuz@gmail.com")  # textbox
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")  # textbox
driver.find_element(By.ID, "exampleCheck1").click()  # checkbox

sel = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
element = driver.find_element(By.ID, "exampleFormControlSelect1")
driver.execute_script("arguments[0].scrollIntoView();", element)
sel.select_by_visible_text("Female")

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Dogukan YAVUZ")
assert "Success" in message

time.sleep(2)
