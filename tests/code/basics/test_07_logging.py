import logging

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Set up the WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options)

    yield driver

    # Teardown: quit the WebDriver after the test
    driver.quit()


def test_open_google(driver):
    LOGGER = logging.getLogger(__name__)
    driver.get("https://www.google.com")
    LOGGER.info('logs - info')
    LOGGER.warning('logs- warning')
    LOGGER.error('logs - error')
    LOGGER.critical('logs - critical')

