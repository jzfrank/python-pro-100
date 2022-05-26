from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 

import random 

import time 


chrome_driver_path = "/Users/zhangjin/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(url)

bigCoockie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")

t_start = time.time()
t_end = time.time() + 60 * 20
cnt = 1
while True:
    # print((time.time() - t_start) % 5)
    # print(cnt * 5)
    # print(int(time.time() - t_start) % int(cnt + 5))
    if (int(time.time() - t_start) % 10 == 0):
        cnt += 1 
        unlocked = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked")
        if unlocked:
            priority = unlocked[-1]
            if "disabled" not in priority.get_attribute("class"):
                priority.click()
                random.choice(unlocked).click()
    bigCoockie.click()


input()

driver.quit()
