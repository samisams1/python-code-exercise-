import feedparser

def read_feed(url):
    feed = feedparser.parse(url)
    for entry in feed.entries:
        print(entry.title)

read_feed("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")