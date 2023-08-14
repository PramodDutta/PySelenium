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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_idrive():
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
    driver.get("https://www.idrive360.com/enterprise/login")

    username = driver.find_element(By.NAME, "username")
    username.send_keys("augtest_040823@idrive.com")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("123456")

    # submit_button = driver.find_element(By.ID, "frm-btn")
    submit_button = driver.find_element(By.CSS_SELECTOR, "#frm-btn")
    submit_button.click()

    add_button = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@id='add-device-header-btn']"))
    )

    add_button.click()

    download_btn = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='id-card-bdy-backup-agent-mac']/button"))
    )
    download_btn.click()

    time.sleep(100)

    # Chrome Dir -> Download
    # Install Software, call a bat file , sh linux
