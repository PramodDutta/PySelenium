import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    # Read a File, Read from DB, Create Webdriver


@pytest.mark.usefixtures("driver")
def test_js_execute(driver):
    URL = "https://www.flipkart.com/"
    driver.get(URL)
    time.sleep(5)
    driver.maximize_window()

    button_cross = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
    actions = ActionChains(driver)
    actions.move_to_element(button_cross).click().perform()

    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys("AC")

    # SVG - G - PATH
    # SVG, G, G, ,G PATH

    search_svg_icon = driver.find_element(By.XPATH,
                                          "//*[local-name()='svg']/*[local-name()='g' and @fill-rule='evenodd']")
    actions = ActionChains(driver)
    actions.move_to_element(search_svg_icon).click().perform()
    time.sleep(5)
