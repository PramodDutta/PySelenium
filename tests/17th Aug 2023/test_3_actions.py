import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_03_actions():
    driver = webdriver.Chrome()
    URL = "https://www.makemytrip.com/"
    driver.get(URL)
    driver.maximize_window()

    time.sleep(5)

    fromCity = driver.find_element(By.ID, "fromCity")
    actions = ActionChains(driver)
    actions.move_to_element(fromCity).click().send_keys("New Delhi").perform()

