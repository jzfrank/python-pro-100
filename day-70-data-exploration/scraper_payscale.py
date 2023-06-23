from bs4 import BeautifulSoup
import requests
import pandas as pd


ranks = []
majors = []
earlyCareerPays = []
midCareerPays = []

for page in range(1, 34+1):
    # Get the HTML from the URL
    url = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page}"
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table", "data-table")
    table_body = table.tbody
    rows = table_body.find_all("tr")
    row = rows[0]

    for row in rows:
        cells = row.find_all("td")
        rank = int(cells[0].find("span", "data-table__value").text)
        major = cells[1].find("span", "data-table__value").text
        earlyCareer = int(cells[3].find(
            "span", "data-table__value").text.replace(",", "")[1:])
        midCareer = int(cells[4].find(
            "span", "data-table__value").text.replace(",", "")[1:])
        ranks.append(rank)
        majors.append(major)
        earlyCareerPays.append(earlyCareer)
        midCareerPays.append(midCareer)

df = pd.DataFrame({
    "Rank": ranks,
    "Major": majors,
    "Early Career Pay": earlyCareerPays,
    "Mid-Career Pay": midCareerPays
})

df.to_csv("payscale2023.csv", index=False)

print(df)
