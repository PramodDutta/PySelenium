from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_tables():
    driver = webdriver.Firefox()
    driver.get("https://awesomeqa.com/webtable.html")
    # driver.maximize_window()

    # Row
    # //table[contains(@id,"cust")]/tbody/tr
    # //div[@role='table']/div[2]/div[9]/div[1]/div[4]
    row_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")
    row = len(row_elements)
    print(row)

    # Col
    # // table[contains( @ id, "cust")] / tbody / tr[2] / td
    col_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)

    # FP - //table[contains(@id,"cust")]/tbody/tr[
    # 7 - i ( 2,7)
    # SP - ]/td[
    # 3 - j ( 1,3)
    # TP - ]


    # //div[@role='table']/div[2]/div[9]/div[1]/div[4]
    # fp - //div[@role='table']/div[2]/div[
    # 1-9
    # sp - ]/div[1]/div[
    # 1- 9
    # tp ]


    #
    # for i in range(1,10)
    # //div[@role='table']/div[2]/div[i]/div[1]/div[3]/following-sibling::div[3]



    first_part = "//table[contains(@id,'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row + 1):  # range(1,10) -> 1, 9+1)
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennet is in {country_text}")

    #Find Helen Bennett's country

    driver.get("https://awesomeqa.com/webtable1.html")
    # Get the table
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")
    row_table = table.find_elements(By.TAG_NAME, "tr")  # //table[@summary='Sample Table']/tbody/tr[4]/td

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME, "td")
        for e in cols:
            if "UAE" in e.text:
                print("Yes")

