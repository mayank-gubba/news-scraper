from bs4 import BeautifulSoup
import requests
import csv

source1 = requests.get('https://www.indiatoday.in/').text

csv_file= open('trending.csv','w')
csv_writer=csv.writer(csv_file)

soup1 = BeautifulSoup(source1, 'lxml')

trending1=soup1.find('div', class_='col-sm-4 col-md-4 col-lg-3 home-top-story')

i=0
for top in trending1.find('ul', class_='itg-listing'):
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


source2 = requests.get('https://www.ndtv.com/latest').text

soup2 = BeautifulSoup(source2, 'lxml')

trending2=soup2.find('div', class_='newins_widget marginb50')
i=0
for top in trending2.find('ul'):
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
