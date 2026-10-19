from bs4 import BeautifulSoup
import requests


# ---------------------------------------------------------
# 1. FETCH HACKER NEWS WEBPAGE
# ---------------------------------------------------------

URL = "https://news.ycombinator.com/"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")


# ---------------------------------------------------------
# 2. EXTRACT ARTICLE TITLES, URLS AND SCORES
# ---------------------------------------------------------

articles = soup.find_all("span", class_="titleline")
scores = soup.find_all("span", class_="score")

article_list = []

for article, score in zip(articles, scores):

    link = article.find("a")

    title = link.get_text(strip=True)
    url = link.get("href")
    points = int(score.get_text().split()[0])

    # Store article information as a tuple
    article_list.append((title, url, points))


# ---------------------------------------------------------
# 3. SORT ARTICLES BY SCORE (HIGHEST FIRST)
# ---------------------------------------------------------

top_10 = sorted(
    article_list,
    key=lambda article: article[2],
    reverse=True
)[:10]


# ---------------------------------------------------------
# 4. DISPLAY TOP 10 ARTICLES
# ---------------------------------------------------------

for position, (title, url, score) in enumerate(top_10, start=1):

    print(f"{position}. WEBPAGE NAME: {title}")
    print(f"   SCORE: {score} points")
    print(f"   URL: {url}\n")