from selenium import webdriver


# Chrome -> # Chrome Options
# Chrome Options  - Chrome with the Extension, Window Size, Proxy, JS disabled

def test_login():
    chrome_options = webdriver.ChromeOptions()

    extension_path = "/Users/pramod/Downloads/adblocker1.crx"
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_extension(extension_path)

    # 1. Headless mode: Run Chrome in headless mode (without GUI)
    chrome_options.add_argument("--headless=new")

    # With UI - slow and consume lot of resource, You can see the Test - 100 -
    # Without UI - headless - fast, it will consume less resources, You can't see the Test > 10,000

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://app.vwo.com")
