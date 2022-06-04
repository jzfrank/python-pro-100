from bs4 import BeautifulSoup 
import lxml 
import requests 

responses = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/",
    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36", 
             "Accept-Language": "en-US,en;q=0.9"})
website_html = responses.text 
soup = BeautifulSoup(website_html, "lxml")


all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]

print(movie_titles[::-1])

with open("movies.txt", "w") as fh:
    for i in range(len(movie_titles) - 1, -1, -1):
        fh.write(movie_titles[i] + "\n")
