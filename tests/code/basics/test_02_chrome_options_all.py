from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create ChromeOptions instance
chrome_options = Options()

# Add options to ChromeOptions

# 1. Headless mode: Run Chrome in headless mode (without GUI)
chrome_options.add_argument('--headless')

# 2. Proxy: Set the proxy server
proxy_server = "http://your_proxy_ip:your_proxy_port"
chrome_options.add_argument('--proxy-server=' + proxy_server)

# 3. User-Agent: Set the user-agent string
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
chrome_options.add_argument(f'user-agent={user_agent}')

# 4. Window size: Set the initial window size
chrome_options.add_argument('--window-size=1366x768')

# 5. Disable extensions: Disable loading of extensions
chrome_options.add_argument('--disable-extensions')

# 6. Disable notifications: Disable showing of notifications
chrome_options.add_argument('--disable-notifications')

# 7. Incognito mode: Start Chrome in incognito (private browsing) mode
chrome_options.add_argument('--incognito')

# 8. Disable GPU: Disable GPU acceleration
chrome_options.add_argument('--disable-gpu')

# 9. Disable images: Disable loading of images
chrome_options.add_argument('--blink-settings=imagesEnabled=false')

# 10. Disable JavaScript: Disable JavaScript execution
chrome_options.add_argument('--disable-javascript')

# 11. Disable infobars: Disable "Chrome is being controlled by automated test software" infobar
chrome_options.add_argument('--disable-infobars')

# 12. Disable browser-side navigation: Disable the browser's ability to handle navigation
chrome_options.add_argument('--disable-web-security')

# 13. User data directory: Set a custom user data directory (for using existing Chrome profile)
chrome_options.add_argument('--user-data-dir=/path/to/user/profile')

# 14. Enable verbose logging: Enables verbose logging for debugging
chrome_options.add_argument('--enable-logging')

# 15. Additional arguments: You can add other specific Chrome command-line arguments as needed
chrome_options.add_argument('--some-specific-argument')

# Create a new instance of the Chrome driver with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the desired URL
driver.get("https://example.com")

# Now you can interact with the web page using the specified options
