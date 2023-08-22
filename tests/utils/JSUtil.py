from selenium.webdriver.support.ui import WebDriverWait


class JSUtils:
    def __init__(self, driver):
        self.driver = driver

    def make_alert(self, msg):
        js = self.driver.execute_script
        js("alert('" + msg + "')")

    def click_element_by_js(self, element):
        try:
            executor = self.driver.execute_script
            executor("arguments[0].click();", element)
        except Exception as e:
            raise AssertionError("Test failed with exception ---> " + str(e))

    def refresh_browser_by_js(driver):
        js = driver.execute_script
        js("history.go(0)")

    def wait_for_page_load(self):
        def page_load_condition(driver):
            return self.driver.execute_script("return document.readyState") == "complete"

        wait = WebDriverWait(self.driver, 5000)
        wait.until(page_load_condition)
        print("*****Page loaded successfully*****")

    def wait_for_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())

    def scroll_into_view(element, driver):
        js = driver.execute_script
        js("arguments[0].scrollIntoView(true);", element)
