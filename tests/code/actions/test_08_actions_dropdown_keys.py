import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_09_actions(driver):
    URL = "https://awesomeqa.com/selenium/action_dropdown.html"
    driver.get(URL)
    driver.maximize_window()

    actions = ActionChains(driver)
    driver.implicitly_wait(5)  # Add an implicit wait

    fromCity = driver.find_element(By.ID, "dropdownMenuButton1")
    actions.move_to_element(fromCity).click().send_keys(Keys.DOWN).send_keys(Keys.DOWN).perform()

if __name__ == "__main__":
    pytest.main([__file__])
