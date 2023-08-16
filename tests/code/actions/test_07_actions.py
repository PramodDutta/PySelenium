import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_07_actions(driver):
    driver.get("https://www.spicejet.com/")
    action = ActionChains(driver)
    element = driver.find_element(By.CSS_SELECTOR, "div[data-testid='to-testID-origin'] > div > div > input")
    action.move_to_element(element).click().perform()

    # Waiting to keep the browser window open for demonstration purposes
    # element.send_keys("DEL")

if __name__ == "__main__":
    pytest.main([__file__])
