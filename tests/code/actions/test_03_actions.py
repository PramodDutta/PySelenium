from time import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium import webdriver

def test_pauses():
    driver = webdriver.Chrome()
    driver.get('https://awesomeqa.com/selenium/mouse_interaction.html')

    start = time()

    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver)\
        .move_to_element(clickable)\
        .pause(1)\
        .click_and_hold()\
        .pause(1)\
        .send_keys("abc")\
        .perform()

    duration = time() - start
    assert duration > 2
    assert duration < 3


def test_releases_all():
    driver = webdriver.Chrome()
    driver.get('https://awesomeqa.com/selenium/mouse_interaction.html')

    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver)\
        .click_and_hold(clickable)\
        .key_down(Keys.SHIFT)\
        .key_down("a")\
        .perform()

    ActionBuilder(driver).clear_actions()

    ActionChains(driver).key_down('a').perform()

    assert clickable.get_attribute('value')[0] == "A"
    assert clickable.get_attribute('value')[1] == "a"