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


def test_idrive():
    LOGGER = logging.getLogger(__name__)
    # Selenium API - Create Session
    driver = webdriver.Chrome()

    driver.maximize_window()

    # Open the Browser
    # Navigate to a URL
    # Command - driver.get ( Navigate command to Existing Session)
    driver.get("https://www.idrive360.com/enterprise/login")

    username = driver.find_element(By.NAME, "username")
    username.send_keys("augtest_040823@idrive.com")

    password = driver.find_element(By.NAME, "password")

    password.send_keys("123456")

    submit_button = driver.find_element(By.ID, "frm-btn")
    submit_button.click()

    time.sleep(15)

    add_button = driver.find_element(By.ID, "add-device-header-btn")
    add_button.click()
    time.sleep(3)
    download_btn = driver.find_element(By.XPATH, "//*[@id='id-card-bdy-backup-agent-mac']/button")
    download_btn.click()

    # Chrome Dir -> Download
    # Install Software, call a bat file , sh linux

