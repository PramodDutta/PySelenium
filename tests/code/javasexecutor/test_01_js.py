import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    # Close the web driver
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_js_execute(driver):
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    driver.get(URL)
    jsExecutor = driver.execute_script

    # Find an element
    element = driver.find_element(By.CSS_SELECTOR, "button[onclick=\"addElement()\"]")
    # Use the JavaScript Executor to click the element
    jsExecutor("arguments[0].click();", element)

    TitleName = jsExecutor("return document.title;")
    jsExecutor("window.scrollBy(0,600)")

    added = driver.find_elements(By.CLASS_NAME, "added-manually")
    print(TitleName)
    print(len(added))

if __name__ == "__main__":
    pytest.main([__file__])
