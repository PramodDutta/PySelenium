# Open the Browser
# Navigate to a URL
# Find the Email WebElement and put email id = “abc@gmail.com”
# Find the Password input box and enter the password = 123
# Click on the button - Sign in


# Verify that the Dashboard is loaded - PyTest
# Create a Report to send to QA Lead - HTML --> Allure Report

import logging

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_vwologin2():
    LOGGER = logging.getLogger(__name__)
    # Selenium API - Create Session
    driver = webdriver.Chrome()

    driver.maximize_window()

    # Open the Browser
    # Navigate to a URL
    # Command - driver.get ( Navigate command to Existing Session)
    driver.get("https://app.vwo.com")

    # find_element by_link_text: Finds an anchor element (a) by its visible text.
    # find_element by_partial_link_text: Finds an anchor element (a) by a partial match of its visible text.

    # <a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">
    # Start a free trial
    # </a>

    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"

    # ID, NAME, CLASS NAME, LINK, Partial, css selector, xpath
    # css selector  > xpath - True / False
    # Which OS, Browser -> 2 GB RAM, now day 8 GM,
    # CSS Selector, Xpath is very small.
    # Use which ever you are comfortable.

    #link = driver.find_element(By.LINK_TEXT, "Start a free trial")
    link = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    link.click()
