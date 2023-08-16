import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_exceptions_demo(driver):
    # Open a webpage
    driver.get("http://app.vwo.com")

    with pytest.raises(NoSuchElementException):
        # Find an element that does not exist on the page
        element = driver.find_element(By.ID, "nonexistent-element")
        element.click()

    # ... Add more tests for other exceptions
