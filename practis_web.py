import requests
from bs4 import BeautifulSoup
websiteUrl=requests.get("https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area").text

soup = BeautifulSoup(websiteUrl,'lxml')
# print(soup.prettify())

My_table = soup.find('table',{'class':'wikitable sortable'})
links=My_table.findAll('a')
# print (links)
countries=[]
for link in links:
    countries.append(link.getText('titel'))
    # countries_name = (link.getText('titel'))
    # print countries_name
    # countries.append(countries_name)
print countries

with open('lele.txt', 'w') as f:
    for item in countries:
        f.write("%s\n" % item)
