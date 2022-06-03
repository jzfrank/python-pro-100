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

# Because there are multiple steps to this Selenium bot, 
# it's easier if we make our code organised using a class.


class InternetSpeedTwitterBot():
    def __init__(self):
        chrome_driver_path = "/Users/zhangjin/Development/chromedriver"
        # self.driver = webdriver.Chrome(service=Service(chrome_driver_path))
        self.driver = uc.Chrome()
        self.download_speed = None
        self.upload_speed = None

    def quit(self):
        self.driver.quit()

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        self.driver.get(url)
        try:
            accept_button = self.driver.find_element(By.CSS_SELECTOR, 
                                                     "#onetrust-accept-btn-handler")
            accept_button.click()
        except Exception as e:
            print(e)
            print(traceback.format_exc())

        time.sleep(2)
        go_button = self.driver.find_element(By.CSS_SELECTOR, 
                                             "#container div div.main-content div div div "
                                             "div.pure-u-custom-speedtest div.speedtest-container.main-row"
                                             " div.start-button a span.start-text")

        go_button.click()
        time.sleep(60)
        print("Waiting Time Finished")
        self.download_speed = self.driver.find_element(By.XPATH, 
                                                       '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
                                                       ).text
        self.upload_speed = self.driver.find_element(By.XPATH, 
                                                     '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'
                                                     ).text       
        print(f'''fetched speed successfully: 
            download_speed: {self.download_speed}, 
            upload_speed: {self.upload_speed}''')

    def tweet_at_provider(self):
        url = "https://twitter.com/i/flow/login"
        self.driver.get(url)
        print(self.driver.window_handles, len(self.driver.window_handles))
        time.sleep(8)
        tmp = self.driver.find_element(By.CSS_SELECTOR, "#react-root")
        print(tmp)
        sign_in_google_button = self.driver.find_element(By.CSS_SELECTOR, 
                                                         "div.css-1dbjc4n.r-eu3ka.r-ywje51.r-usiww2.r-1ipicw7"
                                                         )
        sign_in_google_button.click()

        time.sleep(3)
        print(self.driver.window_handles, len(self.driver.window_handles))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        email_input = self.driver.find_element(By.XPATH, 
                                               "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
        email_input.send_keys(os.environ["GOOGLE_MAIL"])
        confirm_button = self.driver.find_element(By.CSS_SELECTOR, 
                                                  "#identifierNext div button span")
        confirm_button.click()
        time.sleep(3)
        print(self.driver.window_handles, len(self.driver.window_handles))
        password_input = self.driver.find_element(By.CSS_SELECTOR, 
                                                  "#password div.aCsJod.oJeWuf div div.Xb9hP input")
        password_input.send_keys(os.environ["GOOGLE_PSWD"])
        confirm_button = self.driver.find_element(By.CSS_SELECTOR, 
                                                  "#passwordNext div button span")
        confirm_button.click()

        time.sleep(5)
        print(self.driver.window_handles, len(self.driver.window_handles))
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
        tweet_input = self.driver.find_element(By.CSS_SELECTOR, 
                                               '#react-root div div div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 main div div div div div div.css-1dbjc4n.r-14lw9ot.r-184en5c div div.css-1dbjc4n.r-14lw9ot.r-oyd9sg div:nth-child(1) div div div div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t div.css-1dbjc4n.r-184en5c div div div div div div div div div label div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 div div div div div.DraftEditor-editorContainer div div div div'
                                               )
        if self.upload_speed == None:
            raise ValueError("Not run speed test yet. The upload_speed is 0")

        message = f'''WOKO! My internet speed is download_speed {self.download_speed} 
        and upload_speed {self.upload_speed} MB/sec. Why it is so fucking slow? '''
        print(message)
        tweet_input.send_keys(message)
        time.sleep(1)
        privacy_setting = self.driver.find_element(By.CSS_SELECTOR, 
                                                   '#react-root div div div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 main div div div div div div.css-1dbjc4n.r-14lw9ot.r-184en5c div div.css-1dbjc4n.r-14lw9ot.r-oyd9sg div:nth-child(1) div div div div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t div.css-1dbjc4n.r-1awozwy.r-j5o65s.r-qklmqi.r-18u37iz.r-1w6e6rj.r-htfu76.r-13qz1uu div div div div div span span')
        privacy_setting.click()
        print(self.driver.window_handles, len(self.driver.window_handles))
        time.sleep(2)
        only_people_you_mention = self.driver.find_element(By.CSS_SELECTOR, 
                                                           '#layers div.css-1dbjc4n.r-1p0dtai.r-1d2f490.r-105ug2t.r-u8s1d.r-zchlnj.r-ipm5af div div div.css-1dbjc4n.r-u8s1d div div:nth-child(2) div div div div div div:nth-child(2) div:nth-child(3) div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 div span')
        only_people_you_mention.click()

        tweet_button = self.driver.find_element(By.CSS_SELECTOR, 
                                                '#react-root div div div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 main div div div div div div.css-1dbjc4n.r-14lw9ot.r-184en5c div div.css-1dbjc4n.r-14lw9ot.r-oyd9sg div:nth-child(1) div div div div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t div:nth-child(3) div div div:nth-child(2) div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr'
                                                )
        tweet_button.click()
        input()


if __name__ == "__main__":
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
    bot.quit()
