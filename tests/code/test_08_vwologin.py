import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(object):

    @pytest.fixture
    def driver(self):
        self.LOGGER = logging.getLogger(__name__)
        self.driver = webdriver.Chrome()
        yield self.driver
        # Tear Down
        self.driver.quit()

    def test_vwo_login_negative(self, driver):
        driver.get("https://app.vwo.com")

        # Locate and interact with the username and password fields
        username_field = driver.find_element(By.ID, "login-username")
        password_field = driver.find_element(By.ID, "login-password")
        login_button = driver.find_element(By.ID, "js-login-btn")

        # Enter your login credentials
        username_field.send_keys("93npu2yyb0@esiix.co")
        password_field.send_keys("Wingidy@123")

        # Click the login button to submit the form
        login_button.click()

        time.sleep(5)
        notification_box_msg = driver.find_element(By.ID, "js-notification-box-msg")

        self.LOGGER.info("notification_box_msg -> " + notification_box_msg.text)
        assert "Your email, password, IP address or location did not match" in notification_box_msg.text  # Replace "Dashboard" with a string you expect to see after successful login

    def test_vwo_login_negative_2(self, driver):
        driver.get("https://app.vwo.com")

        # Locate and interact with the username and password fields
        username_field = driver.find_element(By.ID, "login-username")
        password_field = driver.find_element(By.ID, "login-password")
        login_button = driver.find_element(By.ID, "js-login-btn")

        # Enter your login credentials
        username_field.send_keys("93npu2yyb0@esiix.co")
        password_field.send_keys("Wingidy@123")

        # Click the login button to submit the form
        login_button.click()

        time.sleep(5)
        notification_box_msg = driver.find_element(By.ID, "js-notification-box-msg")

        self.LOGGER.info("notification_box_msg -> " + notification_box_msg.text)
        assert "Your email, password, IP address or location did not match" in notification_box_msg.text  # Replace "Dashboard" with a string you expect to see after successful login
