import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class GoogleSearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Generally do not assert within pages or components.
        # Effectively throws an exception if the lambda condition is not met.
        WebDriverWait(driver, timeout=5).until(EC.presence_of_element_located((By.ID, "hplogo")))

    def set_click_search_string(self, sstr):
        search_box = self.driver.find_element(By.CSS_SELECTOR, ".gLFyf")
        search_box.send_keys(sstr + Keys.RETURN)
        return self


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("driver_init")
class TestGoogleSearch:
    def test_google_search(self):
        google_page = GoogleSearchPage(self.driver)
        google_page.set_click_search_string("The Testing Academy")


if __name__ == "__main__":
    pytest.main(["-v", "test_fluentapis.py"])
