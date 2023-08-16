import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with


@pytest.fixture
def setup_teardown():
    # Create a new Firefox driver instance
    driver = webdriver.Firefox()

    driver.get("https://awesomeqa.com/selenium/relative.html")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.switch_to.frame(driver.find_element(By.ID, "pollution"))
    yield driver
    driver.quit()


def test_relative_locator_with(setup_teardown):
    driver = setup_teardown

    search_element = driver.find_element(By.ID, "search_city")

    actions = ActionChains(driver)
    actions.move_to_element(search_element).click().send_keys("India" + Keys.RETURN).perform()

    time.sleep(5)

    list_elements = driver.find_elements(By.XPATH, "//table[@id='example']/tbody/tr/td[2]")
    s_values_dict = {}
    for element in list_elements:
        if "India" in element.text:
            print(element.text + "\t")
            s = driver.find_element(locate_with(By.TAG_NAME, "p").to_right_of(element)).text
            s1 = driver.find_element(locate_with(By.TAG_NAME, "p").to_left_of(element)).text
            print(s)
            print(s1)
            s_values_dict[element.text] = int(s)

    # Wait for a brief moment to see the action
    time.sleep(5)

    max_person_name = max(s_values_dict, key=s_values_dict.get)
    max_s_value = s_values_dict[max_person_name]
    print("Max Polluted City -> " + max_s_value, max_person_name)
