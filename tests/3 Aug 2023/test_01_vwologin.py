# Open the Browser
# Navigate to a URL
# Find the Email WebElement and put email id = “abc@gmail.com”
# Find the Password input box and enter the password = 123
# Click on the button - Sign in


# Verify that the Dashboard is loaded - PyTest
# Create a Report to send to QA Lead - HTML --> Allure Report

import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwologin():
    LOGGER = logging.getLogger(__name__)
    # Selenium API - Create Session
    driver = webdriver.Chrome()

    driver.maximize_window()

    # Open the Browser
    # Navigate to a URL
    # Command - driver.get ( Navigate command to Existing Session)
    driver.get("https://app.vwo.com")

    # Find the Email WebElement and put email id = “abc@gmail.com”
    # Find the Password input box and enter the password = 123
    # Click on the button - Sign in

    # < input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    # Selenium - How to find the elements
    # find_element by_id: Finds an element by its unique id attribute.
    # find_element by_name: Finds an element by its name attribute.
    # find_element by_link_text: Finds an anchor element (a) by its visible text.
    # find_element by_partial_link_text: Finds an anchor element (a) by a partial match of its visible text.
    # find_element by_tag_name: Finds an element by its HTML tag name (e.g., "div", "input", "a", etc.).
    # find_element by_class_name: Finds an element by its CSS class name.

    email_address_ele = driver.find_element(By.ID, "login-username")
    password_ele = driver.find_element(By.NAME, "password")

    sign_in_button_ele = driver.find_element(By.ID, "js-login-btn")

    # Sending the data email and password and clicking on the button
    # sendKeys and click()
    email_address_ele.send_keys("93npu2yyb0@esiix.com")
    password_ele.send_keys("Wingify@123")

    sign_in_button_ele.click()

    time.sleep(5)

    # There is delay for 2-3
    LOGGER.info('title is ->  ' + driver.title)
    assert "Dashboard" in driver.title

    driver.refresh()
    driver.get("https://sdet.live")
    driver.back()
    driver.forward()
