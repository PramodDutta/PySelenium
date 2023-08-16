import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    # Close the web driver
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_02_windows_actions_complex(driver):
    URL = "https://app.vwo.com/#/analyze/osa/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1"
    driver.get(URL)
    driver.maximize_window()

    mainWindowHandle = driver.current_window_handle

    ac = ActionChains(driver)
    ac.move_to_element(driver.find_element(By.CSS_SELECTOR, "[data-qa='yedexafobi']")).click().perform()


    time.sleep(20)


    window_handles = driver.window_handles

    # Here we will check if child window has other child windows and will fetch the heading of the child window
    for handle in window_handles:
        if mainWindowHandle != handle:
            driver.switch_to.window(handle)
            driver.switch_to.frame("heatmap-iframe")
            driver.find_element(By.CSS_SELECTOR, "[data-qa='liqokuxuba']").click()



if __name__ == "__main__":
    pytest.main([__file__])
