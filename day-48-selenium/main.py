from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = "/Users/zhangjin/Development/chromedriver"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://www.amazon.de/-/en/NSH006-045496452629-Nintendo-Switch-Console/dp/B0977QC6LN/ref=sr_1_1?&qid=1653284403"
url = "https://www.python.org"
driver.get(url)
event_dates = driver.find_elements_by_css_selector(".last .shrubbery .menu time")
event_names = driver.find_elements_by_css_selector(".last .shrubbery .menu a")
events_date2name = {
    i: {"time": event_dates[i].text, "name": event_names[i].text} 
    for i in range(len(event_dates))
}
print(events_date2name)
# print(event_dates[0].text)


driver.quit()  # shut down the whole browser 
