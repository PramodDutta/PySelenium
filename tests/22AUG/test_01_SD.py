import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.utils.JSUtil import JSUtils

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    # Read a File, Read from DB, Create Webdriver


@pytest.mark.usefixtures("driver")
def test_js_execute(driver):
    URL = "https://selectorshub.com/xpath-practice-page/"
    driver.get(URL)
    div = driver.find_element(By.XPATH, "//div[@class='jackPart']")
    driver.execute_script("arguments[0].scrollIntoView(true);", div)


    pizza = driver.execute_script("return document.querySelector('div.jackPart').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('input#pizza');")
    # href = pizza.get_attribute("href")
    pizza.send_keys("Farmhouse")

    time.sleep(4)