import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
def test_02_actions():
    driver = webdriver.Chrome()
    driver.get('https://awesomeqa.com/selenium/mouse_interaction.html')

    # Click - Normal and action will performed
    # click and hold - click and hold -> click but we will not release.

    driver.find_element(By.ID, "click").click()

    # Action Builder -> Mouse - back
    actions_builder = ActionBuilder(driver)
    actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    actions_builder.perform()




    time.sleep(20)
