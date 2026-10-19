from bs4 import BeautifulSoup
import requests


# ---------------------------------------------------------
# 1. WEBSITE CONFIGURATION
# ---------------------------------------------------------

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-GB,en;q=0.9"
}


# ---------------------------------------------------------
# 2. FETCH AND PARSE WEBPAGE
# ---------------------------------------------------------

response = requests.get(URL, headers=HEADERS, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")


# ---------------------------------------------------------
# 3. EXTRACT MOVIE TITLES
# ---------------------------------------------------------

movies = soup.select('span[data-test="content"] h2')

movie_list = []

for movie in movies:
    title = movie.get_text(strip=True)

    # Keep only movie titles starting with a ranking number
    # Excludes headings such as "25 — 11" and "10 — 1"
    if title.split(")")[0].isdigit():
        movie_list.append(title)


# ---------------------------------------------------------
# 4. REVERSE MOVIE ORDER (1 TO 100)
# ---------------------------------------------------------

movie_list.reverse()


# ---------------------------------------------------------
# 5. SAVE MOVIES TO A TEXT FILE
# ---------------------------------------------------------

OUTPUT_FILE = "movies_list.txt"

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")

print(f"Successfully saved {len(movie_list)} movies to {OUTPUT_FILE}")