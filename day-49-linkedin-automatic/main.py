from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

import random 
import os 
import time 

chrome_driver_path = "/Users/zhangjin/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
url = "https://www.linkedin.com"
driver.get(url)

# log in
email = driver.find_element(By.CSS_SELECTOR, "#session_key") 
email.send_keys(os.environ["USER_EMAIL"])
password = driver.find_element(By.CSS_SELECTOR, "#session_password")
password.send_keys(os.environ["PASSWORD"])
button = driver.find_element(By.CSS_SELECTOR, "button.sign-in-form__submit-button")
button.click()

time.sleep(0.3)

driver.get(url="https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&geoId="
           "106693272&keywords=sde&location=Switzerland")

time.sleep(1)

print(".jobs-search-results__list "
      "ul li.jobs-search-results__list-item")
job_lists = driver.find_elements(By.CSS_SELECTOR, "ul.jobs-search-results__list "
                                 " li.jobs-search-results__list-item")

print("len(job_lists):", len(job_lists))
total_num = len(job_lists)

for i in range(total_num):
    time.sleep(1)
    job_lists = driver.find_elements(By.CSS_SELECTOR, "ul.jobs-search-results__list "
                                     " li.jobs-search-results__list-item")
    job = job_lists[i]
    try:
        job.click()
        time.sleep(1)
    except Exception as e:
        print(e)
    try:
        easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card")
        easy_apply.click()

        submit = driver.find_element(By.CSS_SELECTOR, ".jobs-easy-apply-content footer button")
        # we only consider one step application
        print("submit.text", submit.text)
        print(submit)
        time.sleep(1)
        if submit.text == "Submit application":
            submit.click()
        else:
            dismiss = driver.find_element(By.CSS_SELECTOR, "button.artdeco-modal__dismiss")
            dismiss.click()
            time.sleep(1)
            discard = driver.find_element(By.CSS_SELECTOR, "button.artdeco-modal__confirm-dialog-btn")
            discard.click()
    except Exception as e:
        print(e)


input()
driver.quit()
