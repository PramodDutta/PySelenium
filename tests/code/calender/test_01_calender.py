import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_calender_simple():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.path2usa.com/travel-companion/")
    select_date(driver, 18, 9, 2024)


def select_date(driver, expected_day, expected_month, expected_year):
    time.sleep(15)
    actions = ActionChains(driver)
    srcoll_to_date_picker = driver.find_element(By.XPATH, "//button[@class='elementor-button elementor-size-sm']")
    driver.execute_script("arguments[0].scrollIntoView();", srcoll_to_date_picker)
    # date_picker = driver.find_element(By.XPATH, "//input[@id='form-field-travel_comp_date']")
    # actions.move_to_element(date_picker).click_and_hold().perform()
    # date_picker.click()

    expected_date = datetime(expected_year, expected_month, expected_day)
    print(expected_date)
    current_date = datetime.today()
    if expected_date < current_date:
        print("Date is Old")
        return
    else:
        current_month = driver.find_element(By.XPATH, "//span[@title='Scroll to increment']")
        while True:
            if expected_year is not current_date.year and expected_month is not current_date.month:
                driver.find_element(By.XPATH, "//span[@class='flatpickr-next-month']").click()
                temp_date1 = "//span[@aria-label='"
                temp_part2 = test_date_format(expected_year, expected_month, expected_day)
                print(temp_part2)
                temp_part3 = "']"
                date_select = f"{temp_date1}{temp_part2}{temp_part3}"
                temp = driver.find_element(By.XPATH, date_select).text
                if temp == "August 18, 2024":
                    print(temp)
                    break


    time.sleep(1000)
    # .flatpickr-prev-month
    # //span[@class='flatpickr-next-month']
    # //span[@title='Scroll to increment']


def test_date_format(expected_year, expected_month, expected_day):
    input_date = f"{expected_year}-{expected_month}-{expected_day}"
    formatted_date = datetime.strptime(input_date, "%Y-%m-%d").strftime("%B %d, %Y")
    return formatted_date
