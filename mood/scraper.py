import requests
from bs4 import BeautifulSoup

def tweet_scraper(user):
    URL = "https://nitter.net/"+user+"/with_replies"
    page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div", class_="tweet-content media-body")
    results = results[0:10]
    tweets = []
    for r in results:
	    if len(r.contents):
		    if r.string is not None:
			    tweets.append(r.string)

    return tweets
                
			    