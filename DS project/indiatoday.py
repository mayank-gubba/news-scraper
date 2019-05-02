from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.indiatoday.in/').text

csv_file= open('indiatoday.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','news_link'])

soup = BeautifulSoup(source, 'lxml')

trending=soup.find('div', class_='col-sm-4 col-md-4 col-lg-3 home-top-story')

i=0
for top in trending.find('ul', class_='itg-listing'):
    if i<3:
        news=top.find('a')['title']
        print(news)
        link=top.find('a')['href']
        flink=f'https://www.indiatoday.in{link}'
        print(flink)
        csv_writer.writerow([news,flink])
    else:
        break
    i=i+1
csv_file.close()
