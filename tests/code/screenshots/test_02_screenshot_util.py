import pytest
from selenium import webdriver
from screenshot_util import ScreenshotUtil

class TakeScreenshotTest():

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://awesomeqa.com/practice.html")
        self.driver.maximize_window()
        self.screenshot_util = ScreenshotUtil(self.driver)

    def test_take_screenshot(self):
        # Provide a name for the screenshot
        screenshot_name = "example_screenshot"

        # Take a screenshot with timestamp at the end
        screenshot_path = self.screenshot_util.take_screenshot(screenshot_name)

        print(f"Screenshot saved to: {screenshot_path}")

    def tearDown(self):
        self.driver.quit()
