from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.indiatoday.in/').text

csv_file= open('indiatoday.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','news_link'])

soup = BeautifulSoup(source, 'lxml')

trending=soup.find('div', class_='col-sm-4 col-md-4 col-lg-3 home-top-story')

for top in trending.find('ul', class_='itg-listing'):


    news=top.find('a')['title']
    print(news)
    link=top.find('a')['href']
    print(link)
    csv_writer.writerow([news,link])

csv_file.close()
