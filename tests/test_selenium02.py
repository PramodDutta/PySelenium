import pytest
from selenium import webdriver
import logging

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    # return driver # Value will be stored permantly, extra variable


def test_open_url_verify_title(driver):
    LOGGER = logging.getLogger(__name__)
    driver.get("https://app.vwo.com")
    print(driver.title)
    # Verification
    # Actual Result == Expected Result
    LOGGER.info("This is information Logs")
    LOGGER.warning("This is Warning Logs")
    LOGGER.error("This is Error Logs")
    LOGGER.critical("This is Critical Logs")
    assert "Login - VWO" == driver.title
