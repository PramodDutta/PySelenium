import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ShadowDOMTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://selectorshub.com/xpath-practice-page/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_shadow_dom_interaction(self):
        actions = ActionChains(self.driver)
        div = self.driver.find_element(By.XPATH, "//div[@class='jackPart']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", div)

        link = self.driver.execute_script("return document.querySelector('div.jackPart').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('input#pizza');")
        print(link.get_attribute("value"))
        link.send_keys("Farmhouse")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
