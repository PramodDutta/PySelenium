import unittest
import os
from selenium import webdriver

class TakeScreenshotTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://awesomeqa.com/practice.html")
        self.driver.maximize_window()

    def test_take_screenshot(self):
        screenshot_path = os.path.join(os.getcwd(), "screenshot.jpg")

        # Take a screenshot and save it to the specified path
        self.driver.save_screenshot(screenshot_path)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
