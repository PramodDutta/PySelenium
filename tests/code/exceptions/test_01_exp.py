from selenium import webdriver
from selenium.webdriver.common.by import By


def test_main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://google.com")
    ele = driver.find_element(By.XPATH,"//*[@class=\"gLFyf\"]")
    driver.refresh()
    ele.send_keys("Testing String")

    driver.quit()

