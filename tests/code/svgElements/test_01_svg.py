import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_svg_demo(driver):
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()

    div = driver.find_element(By.XPATH, "//div[@class='jackPart']")

    # Scroll To View
    driver.execute_script("arguments[0].scrollIntoView(true);", div)

    # Get shadow DOM elements using JavaScript
    input_pizza = driver.execute_script("return document.querySelector('div.jackPart').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('input#pizza');")

    # Perform actions on the shadow DOM element
    input_pizza.send_keys("FarmHouse")
    input_pizza.send_keys(Keys.ENTER)

if __name__ == "__main__":
    pytest.main(["-v"])
