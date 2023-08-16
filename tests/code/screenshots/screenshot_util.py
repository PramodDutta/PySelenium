import os
from selenium import webdriver
from datetime import datetime

class ScreenshotUtil:

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, name="screenshot"):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{name}_{timestamp}.png"
        screenshot_path = os.path.join(os.getcwd(), filename)
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path
