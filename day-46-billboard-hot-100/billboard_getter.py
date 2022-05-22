import requests 
from bs4 import BeautifulSoup
import lxml 


def get_billboard_top100(date):
    responses = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
    soup = BeautifulSoup(responses.text, "lxml")

    top100_songs = soup.select("li.o-chart-results-list__item h3#title-of-a-story.c-title")
    top100_songs = list(map(lambda x: x.getText().strip(), top100_songs))

    top100_singers = soup.select("li.lrv-u-width-100p li.o-chart-results-list__item span.c-label.a-font-primary-s")
    top100_singers = list(map(lambda x: x.getText().strip(), top100_singers))

    assert(len(top100_singers) == 100)
    assert(len(top100_singers) == len(top100_songs))
    top100_singer2song = {top100_singers[i]: top100_songs[i] for i in range(len(top100_singers))}
    return top100_singer2song


if __name__ == "__main__":
    print("We provide service of travelling back with how music at a specific data")
    # date = input("What it the day you want to trace back to?(seperated by -, e.g. 2000-09-02)\n")
    date = "2000-09-02"
    print(date)
    get_billboard_top100(date)
