from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests

session = HTMLSession()

url = 'https://news.google.com/search?q=covid&hl=en-ZA&gl=ZA&ceid=ZA%3Aen'
r = session.get(url)

r.html.render(sleep=1, scrolldown = 10)
articles = r.html.find('article')

# print(articles)

for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        title = newsitem.text
        link = newsitem.absolute_links
        print(title,link)
    except:
        pass


