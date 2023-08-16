from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class JSUtils:
    def __init__(self, driver):
        self.driver = driver

    def make_alert_from_js(self, msg):
        js = self.driver.execute_script
        js("alert('" + msg + "')")

    def click_element_by_jse(self, element):
        try:
            executor = self.driver.execute_script
            executor("arguments[0].click();", element)
        except Exception as e:
            raise AssertionError("Test failed with exception ---> " + str(e))

    @staticmethod
    def refresh_browser_by_js(driver):
        js = driver.execute_script
        js("history.go(0)")

    @staticmethod
    def get_title_by_js(driver):
        js = driver.execute_script
        title = js("return document.title;")
        return title

    @staticmethod
    def get_page_inner_text(driver):
        js = driver.execute_script
        page_text = js("return document.documentElement.innerText;")
        return page_text

    @staticmethod
    def scroll_page_down(driver):
        js = driver.execute_script
        js("window.scrollTo(0,document.body.scrollHeight);")

    @staticmethod
    def scroll_into_view(element, driver):
        js = driver.execute_script
        js("arguments[0].scrollIntoView(true);", element)

    def wait_for_page_load(self):
        def page_load_condition(driver):
            return self.driver.execute_script("return document.readyState") == "complete"

        wait = WebDriverWait(self.driver, 5000)
        wait.until(page_load_condition)
        print("*****Page loaded successfully*****")

    def wait_for_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
