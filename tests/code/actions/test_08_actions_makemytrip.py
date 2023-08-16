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
def test_08_actions_make_mytrip(driver):
    URL = "https://www.makemytrip.com/"
    driver.get(URL)
    driver.maximize_window()

    actions = ActionChains(driver)
    driver.implicitly_wait(5)  # Add an implicit wait

    fromCity = driver.find_element(By.ID, "fromCity")
    actions.move_to_element(fromCity).click().send_keys("New Delhi, India").perform()

    li = driver.find_elements(By.XPATH, "(//ul[@role='listbox'])/li")
    for element in li:
        if "New Delhi, India" in element.text:
            element.click()
            break

    act = ActionChains(driver)
    act.send_keys(Keys.PAGE_DOWN).perform()  # Page Down
    print("Scroll down performed")

if __name__ == "__main__":
    pytest.main([__file__])
