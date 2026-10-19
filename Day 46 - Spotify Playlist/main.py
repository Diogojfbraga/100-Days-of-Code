import requests


URL = 'https://music.youtube.com/'


response = requests.get(URL)

print(response)