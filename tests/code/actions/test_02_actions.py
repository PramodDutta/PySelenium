from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import sys, pytest

@pytest.mark.actions
def test_02_actions():
    # Initialize the Firefox driver
    driver = webdriver.Firefox()

    # URL for the web page
    URL = "https://awesomeqa.com/practice.html"
    driver.get(URL)
    driver.maximize_window()
    cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
    driver.get('https://awesomeqa.com/selenium/single_text_input.html')
    ActionChains(driver) \
        .send_keys("Selenium!") \
        .send_keys(Keys.ARROW_LEFT) \
        .key_down(Keys.SHIFT) \
        .send_keys(Keys.ARROW_UP) \
        .key_up(Keys.SHIFT) \
        .key_down(cmd_ctrl) \
        .send_keys("xvv") \
        .key_up(cmd_ctrl) \
        .perform()

    driver.quit()