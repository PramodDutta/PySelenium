import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
def test_01_windows(driver):
    # Open the page
    driver.get("https://the-internet.herokuapp.com/windows")

    # Store the handle of the current window
    main_window_handle = driver.current_window_handle

    # Find the "Click Here" link
    link = driver.find_element(By.LINK_TEXT, "Click Here")

    # Click the link to open a new window
    link.click()

    # Store the handles of all open windows in a list
    window_handles = driver.window_handles

    # Iterate through the list of window handles
    for handle in window_handles:
        # Switch the focus to each window in turn
        driver.switch_to.window(handle)

        # Check if the text "New Window" is present in the window
        if "New Window" in driver.page_source:
            print("The text 'New Window' was found in the new window.")
            break

    # Switch the focus back to the main window
    driver.switch_to.window(main_window_handle)

if __name__ == "__main__":
    pytest.main([__file__])
