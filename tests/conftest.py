import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import requests


# in order for us to use 'pytest —browser_name chrome’ on terminal, we have to use this code

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="safari"
    )


# request is a special fixture provided by pytest
# it is made for fixtures
# 'request' parameter in a pytest fixture is an object that provides information about the test
@pytest.fixture(scope="class")
def setup(request):
    # Retrieves the value of the 'browser_name' command-line option provided when running the tests.
    # This allows the test to dynamically adjust its behavior based on the specified browser.
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        s = Service('..path/chromedriver')
        driver = webdriver.Chrome(service=s)
    elif browser_name == "safari":
        driver = webdriver.Safari()
    elif browser_name == "IE":
        print("IE")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Attaching the driver to the class that will use this fixture
    request.cls.driver = driver

    yield
    driver.close()
