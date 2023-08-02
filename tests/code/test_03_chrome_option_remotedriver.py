from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Create ChromeOptions instance
chrome_options = webdriver.ChromeOptions()

# Add options to ChromeOptions (same as shown in the previous example)
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1366x768')

# Set desired capabilities with ChromeOptions
desired_capabilities = DesiredCapabilities.CHROME.copy()
desired_capabilities['platform'] = 'ANY'  # Platform can be 'WINDOWS', 'LINUX', etc.
desired_capabilities['version'] = ''  # Version can be empty or specific version like '91.0'

# URL of the Remote WebDriver server
remote_server_url = "http://<remote_server_ip>:<remote_server_port>/wd/hub"

# Create Remote WebDriver instance
driver = webdriver.Remote(command_executor=remote_server_url, desired_capabilities=desired_capabilities, options=chrome_options)

# Navigate to the desired URL
driver.get("https://example.com")

# Now you can interact with the web page using the specified options on the Remote WebDriver
