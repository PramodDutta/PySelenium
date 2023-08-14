import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def test_alerts_testing():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    button = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
    button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Pramod")
    alert.accept()
    # alert.dismiss()

    result = driver.find_element(By.XPATH, "//p[@id='result']")
    print(result.text)



