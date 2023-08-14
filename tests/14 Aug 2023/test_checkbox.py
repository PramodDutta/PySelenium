import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_checkbox_testing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    # cHECK THE CHECKBX WHICH IS NOT SELECTED
    for c in checkboxes:
        if not c.is_selected():
            c.click()

    time.sleep(10)
