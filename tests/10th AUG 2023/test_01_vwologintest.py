# Open the Browser
# Navigate to a URL
# Find the Email WebElement and put email id = “abc@gmail.com”
# Find the Password input box and enter the password = 123
# Click on the button - Sign in


# Verify that the Dashboard is loaded - PyTest
# Create a Report to send to QA Lead - HTML --> Allure Report

import logging

from selenium import webdriver
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_vwologin():
    LOGGER = logging.getLogger(__name__)
    # Selenium API - Create Session
    driver = webdriver.Chrome()
    # driver.implicitly_wait(20)
    # # Tell Webdriver to wait for 20 Seconds to Load - All the elements
    # # What if e1,e2,e3 <  20 waste of time

    driver.maximize_window()

    # Open the Browser
    # Navigate to a URL
    # Command - driver.get ( Navigate command to Existing Session)
    driver.get("https://app.vwo.com/#/login")

    username = driver.find_element(By.NAME, "username")
    username.send_keys("93npu2yyb0@esiix.com")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("Wingify@123")

    # submit_button = driver.find_element(By.ID, "frm-btn")
    submit_button = driver.find_element(By.CSS_SELECTOR, "#js-login-btn")
    submit_button.click()

    # .page-heading

    # WebDriverWait(driver, 10).until(
    #     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-heading"), "Dashboard")
    # )

    # IW and EW ->
    # IW -> Global Wait for all the elements ->  e0 = 1, e2 = 0, e3 = 6,  TT = 9,   IW  = 10 - 1
    # EW - e3 - 10, e1 nad e2

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    element = EC.presence_of_element_located((By.CSS_SELECTOR, ".page-heading"))
    # PF = 1  EF = NO, m > 10 , WD - Should Exception ?
    # PF = 2  EF = NO, m > 10 , WD - Should Exception ?
    #......
    # PF = 10  EF = NO, m = 10 , WD - Should Exception Yes


    # 5 ?

    driver.quit()
