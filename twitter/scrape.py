import requests
from bs4 import BeautifulSoup

user = "elonmusk"
URL = "https://nitter.net/"+user+"/with_replies"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("div", class_="tweet-content media-body")

for r in results:
	if len(r.contents):
		if r.string is not None:
			print(r.string)
			print("~")