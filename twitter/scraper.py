import requests
from bs4 import BeautifulSoup

user = "elonmusk"
URL = "https://nitter.net/%22+user+%22/with_replies"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.findall("div", class_="tweet-content media-body")

for r in results:
    if len(r.contents):
        if r.string is not None:
            print(r.string)
            print("~")