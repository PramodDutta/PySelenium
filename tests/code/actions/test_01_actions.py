import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

@pytest.mark.actions
def test_01_actions():
    # Initialize the Firefox driver
    driver = webdriver.Firefox()

    # URL for the web page
    URL = "https://awesomeqa.com/practice.html"
    driver.get(URL)
    driver.maximize_window()

    FIRSTNAME = driver.find_element(By.NAME, "firstname")

    # Create object of ActionChains class
    actions = ActionChains(driver)

    # This will type Username in Uppercase as we are typing using Shift key pressed
    actions.key_down(Keys.SHIFT)\
        .send_keys_to_element(FIRSTNAME, "the testing academy")\
        .key_up(Keys.SHIFT)\
        .perform()

    date = driver.find_element(By.ID, "datepicker")
    actions.send_keys_to_element(date, "23/12/2025").perform()

    link = driver.find_element(By.XPATH, "//a[contains(text(), 'Click here to Download File')]")
    actions.context_click(link).perform()

    # Quit the driver
    driver.quit()

# Run the test function
if __name__ == "__main__":
    pytest.main([__file__])
