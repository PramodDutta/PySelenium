from selenium import webdriver
import logging
# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open a new URL in another window or tab

driver.get("https://app.vwo.com")

# Close the all window and terminate the WebDriver session entirely
driver.quit()

