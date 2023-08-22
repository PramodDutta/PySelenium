import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.NAME, "firstname")

    # Create Object of Action Chains Class
    actions = ActionChains(driver)
    # Send keys but with the Shift
    # press shift key down
    # press shift key up (release)
    actions \
        .key_down(Keys.SHIFT) \
        .send_keys_to_element(first_name, "the testing academy") \
        .key_up(Keys.SHIFT).perform()

    # the testing academy
    # THE TESTING ACADEMY

    # url = driver.find_element(By.XPATH, "//a[normalize-space()='Click here to Download File']")
    # actions.context_click(url).perform()

    driver.get("https://awesomeqa.com/selenium/single_text_input.html")
    actions.send_keys("Selenium")

    time.sleep(20)
