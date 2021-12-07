from bs4 import BeautifulSoup
import requests
import pandas as pd
SA_news = pd.read_csv('C:/Users/mwamb/Desktop/Desktop/web craping/test.csv',delimiter=',', encoding='cp1252')
#print(SA_news.head())

def scrape_screenplay(url):
    response = requests.get(url)
    html_string = response.text
    return html_string


SA_news['text'] = SA_news['link'].apply(scrape_screenplay)
print(SA_news)


for text in SA_news['text']:
     soup = BeautifulSoup(text, 'html.parser')
    #  print(soup)


     # getting all the paragraphs
     for para in soup.find_all("p"):
         print(para.get_text())
                 
            

#     newsZA = soup.find_all('p')
#     # print(newsZA)
         newsSA = para.get_text()
#     # print(newsSA)
         with open('newsZA.txt', 'a', encoding='utf-8') as f:
             f.write(newsSA)



