from bs4 import BeautifulSoup
import lxml
import requests
import smtplib 
import os 


def get_price():
    url = "https://www.amazon.de/-/en/NSH006-045496452629-Nintendo-Switch-Console/dp/B0977QC6LN/ref=sr_1_1?&qid=1653284403"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36", 
                                          "Accept-Language": "en-US,en;q=0.9",
                                          'referer': 'https://www.amazon.de/'})

    with open("tmp.html", "wb") as f:
        f.write(response.content)
    soup = BeautifulSoup(response.content, "lxml")
    price = soup.select("div#desktop_unifiedPrice span#priceblock_ourprice")[0].getText()[1:]
    price = float(price)
    print(price)
    return price 


def send_mail(msg):
    print("trying to build connection with smtp.gmail.com")
    with smtplib.SMTP_SSL("smtp.gmail.com") as conn:
        print("connection built")
        conn.login(user=os.environ["MY_EMAIL"], password=os.environ["MY_PASSWORD"])
        print("logged")
        conn.sendmail(from_addr=os.environ["MY_EMAIL"], 
                      to_addrs=os.environ["TARGET_EMAIL"], 
                      msg=msg)
        print("email sent")


if __name__ == "__main__":
    msg = '''Subject:Hot Price Alert
    \n\nTime to buy Nintendo-Switch-Console'''
    send_mail(msg)
