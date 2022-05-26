from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 


chrome_driver_path = "/Users/zhangjin/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
url = "https://secure-retreat-92358.herokuapp.com/"
# url = "https://www.appbrewery.co/p/newsletter"
driver.get(url)

fname = driver.find_element(by=By.NAME, value="fName")
fname.send_keys("random_fname")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("random_lname")
email = driver.find_element(By.NAME, "email")
email.send_keys("random_email@asfd")
button = driver.find_element(By.CSS_SELECTOR, ".form-signin .btn")
# button.send_keys(Keys.ENTER)
button.click()

input()

driver.quit()
