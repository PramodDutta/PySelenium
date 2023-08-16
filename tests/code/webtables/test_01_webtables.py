from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtables():
    # Initialize the Firefox driver
    driver = webdriver.Firefox()

    # URL for the web page
    URL = "https://awesomeqa.com/webtable.html"
    driver.get(URL)
    driver.maximize_window()

    # Number of Rows and Columns in the table
    row_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
    col_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td")

    row = len(row_elements)
    col = len(col_elements)

    print(row)
    print(col)

    first_part = "//table[@id='customers']/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    # Loop through rows and columns to print data
    for i in range(2, row + 1):
        for j in range(1, col + 1):
            dynamic_xpath = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_xpath).text
            print(data, end=" ")
        print()

    # Find Helen Bennett's country
    for i in range(2, row + 1):
        for j in range(1, col + 1):
            dynamic_xpath = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_xpath).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_xpath}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path)
                print("------")
                print(f"Helen Bennett is in - {country_text.text}")

    print(" ||||||||||||||||||||||| \n")

    # Navigate to another URL
    driver.get("https://awesomeqa.com/webtable1.html")

    # Get the table
    table = driver.find_element(By.XPATH, ("//table[@summary='Sample Table']/tbody"))
    rows_table = table.find_elements(By.TAG_NAME, ("tr"))

    # Loop through rows and columns to print data
    for row_element in rows_table:
        columns_table = row_element.find_elements(By.TAG_NAME,("td"))
        for element in columns_table:
            print(element.text)

    # Quit the driver
    driver.quit()
