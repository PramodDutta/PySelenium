from selenium import webdriver


def test_login():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    # Set PageLoadStrategy to 'none' (Not a built-in option,
    # but we can use it for reference)
    # Add the proxy to ChromeOptions
    chrome_options.add_argument("--page-load-strategy=none")

    # Add the proxy to ChromeOptions
    proxy_server = "http://your_proxy_ip:your_proxy_port"
    chrome_options.add_argument('--proxy-server=' + proxy_server)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com")
    print(driver.title)
    driver.quit()
