from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import undetected_chromedriver.v2 as uc

import time
import os
import random
import traceback

from price_scraper import get_house_details


if __name__ == "__main__":
    house_details = get_house_details()
    print(f"len(house_details): {len(house_details)}")
    url = "https://docs.google.com/forms/d/e/1FAIpQLSca0eIwdlozLMIunI2MK5LFIOOMbpFEEe7-Y0lXlzHqKw9_jA/viewform?usp=sf_link"
    driver = uc.Chrome()
    driver.get(url)
    for house in house_details:
        try:
            time.sleep(3)
            for i, prop in enumerate(["address", "price", "link"]):
                driver.find_elements(By.CSS_SELECTOR, "input[type='text']")[i].click()
                driver.find_elements(By.CSS_SELECTOR, "input[type='text']")[i].send_keys(
                    house[prop]
                )
            driver.find_element(By.CSS_SELECTOR, "div[role='button']").click()
            driver.find_element(By.PARTIAL_LINK_TEXT, 'another').click()
        except Exception as e:
            print(e)
            traceback.print_exc()

    driver.quit()
