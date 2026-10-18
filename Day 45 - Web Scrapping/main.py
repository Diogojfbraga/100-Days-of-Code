# from bs4 import BeautifulSoup

# with open("website.html") as f:
#     contents = f.read()

# soup = BeautifulSoup(contents, "html.parser")


# all_anchor = soup.find_all(name="a")

# for tag in all_anchor:

#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")

# print(he)


from bs4 import BeautifulSoup
import requests

web_page = requests.get('http://news.ycombinator.com/')

soup = BeautifulSoup(web_page.text, "html.parser")

section = soup.find_all(name='a')

for tag in section:
    print(tag.get('href'))

# print(section)




