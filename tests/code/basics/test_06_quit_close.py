from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the first URL
driver.get("https://app.vwo.com")

# Perform your test scenarios in the first window...
# Close the current browser window, but the WebDriver session remains open
driver.close()

