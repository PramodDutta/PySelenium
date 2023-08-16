import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
from selenium.webdriver.support.relative_locator import locate_with

@pytest.fixture
def setup_teardown():
    # Create a new Firefox driver instance
    driver = webdriver.Firefox()
    driver.get("https://codepen.io/AbdullahSajjad/full/LYGVRgK")
    driver.maximize_window()
    driver.switch_to.frame("result")
    yield driver
    driver.quit()


def test_relative_locator(setup_teardown):
    driver = setup_teardown

    submit = driver.find_element(By.XPATH, "//form[@id='form']/button")
    submit.click()

    element = driver.find_element(By.ID, "username")
    errorElement = driver.find_element(locate_with(By.TAG_NAME,"small").below(element))
    error = errorElement.text
    print(error)
    assert errorElement.is_displayed()

    # Wait for a brief moment to see the action
    time.sleep(5)
