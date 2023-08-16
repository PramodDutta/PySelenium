from selenium import webdriver
from JSUtils import JSUtils
from selenium.webdriver.common.by import By


def test_js_execute(driver):
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    driver.get(URL)

    js_utils = JSUtils(driver)  # Create an instance of JSUtils with the WebDriver instance

    # Find an element
    element = driver.find_element(By.CSS_SELECTOR, "button[onclick=\"addElement()\"]")

    js_utils.click_element_by_jse(element)  # Click the element using JSUtils method

    title = JSUtils.get_title_by_js(driver)  # Get the title using JSUtils method
    print(title)

    page_text = JSUtils.get_page_inner_text(driver)  # Get the page inner text using JSUtils method
    print(page_text)

    js_utils.scroll_page_down(driver)  # Scroll the page using JSUtils method

    js_utils.wait_for_page_load()  # Wait for page to load using JSUtils method

    js_utils.make_alert_from_js("This is an alert!")  # Create an alert using JSUtils method

    js_utils.wait_for_alert()  # Wait for alert to appear using JSUtils method

    js_utils.refresh_browser_by_js(driver)  # Refresh the browser using JSUtils method

    added = driver.find_elements(By.CLASS_NAME, "added-manually")
    print(len(added))


if __name__ == "__main__":
    driver = webdriver.Chrome()
    test_js_execute(driver)
    driver.quit()
