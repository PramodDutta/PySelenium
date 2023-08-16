import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def setup_teardown():
    # Create a new Firefox driver instance
    driver = webdriver.Firefox()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_relative_locator(setup_teardown):
    driver = setup_teardown

    element = driver.find_element(By.XPATH, "//span[.='Years of Experience']")

    # Using relative locators to find and click the element to the right of the target element
    driver.find_element(By.ID, "exp-1").click()

    # Wait for a brief moment to see the action
    try:
        driver.implicitly_wait(5)
    except Exception as e:
        print(e)
