import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_03_actions():
    driver = webdriver.Chrome()
    URL = "https://the-internet.herokuapp.com/windows"
    driver.get(URL)
    driver.maximize_window()

    main_window_handle = driver.current_window_handle
    print(main_window_handle)
    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()

    window_handles = driver.window_handles
    print(window_handles)

    for handle in window_handles:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("Found the Text")
            break

    driver.switch_to.window(main_window_handle)

    time.sleep(10)