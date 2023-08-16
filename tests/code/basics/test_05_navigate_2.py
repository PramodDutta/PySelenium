from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Use navigate.to() to open a URL in the current tab
# This does not exist in Python
#driver.navigate.to("https://app.vwo.com")

# Use get() to open a URL in the current tab
driver.get("https://google.com")
