from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.ndtv.com/latest').text

csv_file= open('ndtv.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','news_link'])

soup = BeautifulSoup(source, 'lxml')

trending=soup.find('div', class_='newins_widget marginb50')
i=0
for top in trending.find('ul'):
    if i<2:
        link=top.find('a')['href']
        print(link)
        headline=top.find('div',class_='description').text
        print(headline)
        csv_writer.writerow([headline,link])
    else:
        break
    i=i+1
csv_file.close()
