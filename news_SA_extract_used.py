from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import csv

session = HTMLSession()

url = 'https://news.google.com/search?q=coronavirus%2C%20South%20Africa&hl=en-ZA&gl=ZA&ceid=ZA%3Aen'
r = session.get(url)

r.html.render(scrolldown = 10)
articles = r.html.find('article')

# print(articles) ``
newslist = []
for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        newsarcticle ={
        'title' : newsitem.text,
        'link' :  newsitem.absolute_links
        }
        newslist.append(newsarcticle)


    except:
        pass
#print(len(newslist))

#print(newslist[0])
field_names = ['title', 'link']
with open('test.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(newslist)


