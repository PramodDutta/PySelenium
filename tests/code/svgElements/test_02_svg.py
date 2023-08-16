import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_svg_demo(driver):
    driver.get("https://flipkart.com")
    driver.maximize_window()
    search_input = driver.find_element(By.NAME, "q")
    search_input.send_keys("AC")

    search_element = driver.find_element(By.XPATH, "//*[local-name()='svg']/*[local-name()='g' and @fill-rule='evenodd']")
    actions = ActionChains(driver)
    actions.move_to_element(search_element).click().perform()

    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    states_list = driver.find_elements(By.XPATH, "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in states_list:
        aria_label = state.get_attribute("aria-label")
        print(aria_label)
        if aria_label == "Tripura  ":
            actions.move_to_element(state).click().perform()
            break

if __name__ == "__main__":
    pytest.main(["-v"])
