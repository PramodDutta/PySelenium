from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the desired URL
driver.get("https://sdet.live")

driver.refresh()

# Go back to the previous page
driver.back()

driver.maximize_window()

driver.minimize_window()

driver.fullscreen_window()

current_url = driver.current_url
print("Current URL:", current_url)

new_url = "https://sdet.live/become"
driver.execute_script(f"window.location.href='{new_url}'")

driver.quit()