from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)

soup = BeautifulSoup(html_text,'lxml')
#jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')


job = soup.find('li',class_='clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_ ='joblist-comp-name').text.replace(' ','')
# print(company_name)

#skills = job.find('span', class_='srp-skills')
#skills = job.find('span', class_='srp-skills').text

skills = job.find('span', class_='srp-skills').text.replace(' ','')
#print(skills)

published_date = job.find('span', class_='sim-posted').span.text
print(published_date)



# print(f''' 
# company Name :{company_name}
# Required Skills : {skills}

# ''')
