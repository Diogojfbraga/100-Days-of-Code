
import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------------
# 1. WEBSITE CONFIGURATION
# ---------------------------------------------------------

YOUTUBE_URL = 'https://music.youtube.com/'

list_date = str(input("chose a Date format 'YYYY-MM-DD': "))

BILLIBOARD_URL = f'https://appbrewery.github.io/bakeboard-hot-100/{list_date}/'


# ---------------------------------------------------------
# 2. FETCH AND PARSE BILLBOARD WEBPAGE
# ---------------------------------------------------------

response = requests.get(BILLIBOARD_URL)

soup = BeautifulSoup(response.text, 'html.parser')


# ---------------------------------------------------------
# 3. EXTRACT SONG TITLES AND ARTISTS
# ---------------------------------------------------------

my_songs = []

titles = soup.find_all('h3', class_='chart-entry__title')
artists = soup.find_all('span', class_='chart-entry__artist')

for title, artist in zip(titles, artists):
    music_title = title.get_text()
    artists_name = artist.get_text()

    my_songs.append((music_title, artists_name))


# ---------------------------------------------------------
# 4. DISPLAY EXTRACTED SONGS
# ---------------------------------------------------------

print(my_songs)
