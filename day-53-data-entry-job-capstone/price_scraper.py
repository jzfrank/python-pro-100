from bs4 import BeautifulSoup 
import lxml 
import requests 
import traceback
import joblib


def get_house_details():
    house_details = []
    for page_num in range(1, 5 + 1):
        url = f"https://www.zillow.com/new-york-ny/rentals/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A{page_num}%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.51793966749032%2C%22east%22%3A-73.20576010206064%2C%22south%22%3A40.51489666331152%2C%22north%22%3A40.97476721040177%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A692473%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
        session = requests.Session()
        responses = session.get(url=url, 
                                headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36", 
                                         "Accept-Language": "en-US,en;q=0.9"})
        website_html = responses.text 
        soup = BeautifulSoup(website_html, "lxml")

        with open("tmp.html", "w") as fh:
            fh.write(str(soup))

        card_info_list = soup.find_all(class_ = "list-card-info")
        print("len(card_info_list)", len(card_info_list))
        for i, card_info in enumerate(card_info_list):
            print(i, end=",")
            try:
                address = card_info.find(class_ = "list-card-addr").text
                price = card_info.find(class_="list-card-price").text
                link = "https://www.zillow.com" + card_info.find(class_="list-card-link")["href"]
                house_details.append({
                    "address": address,
                    "price": price,
                    "link": link
                })
            except Exception as e:
                print(e)

    return house_details


if __name__ == "__main__":
    house_details = get_house_details()
    print(house)
