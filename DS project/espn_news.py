from bs4 import BeautifulSoup
import requests
import csv

#hindustantimes
source1 = requests.get('https://www.hindustantimes.com/sports-news/').text

csv_file= open('sports.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','news_link'])

soup1 = BeautifulSoup(source1, 'lxml')

trending1=soup1.find('div', class_='banner-thumbs')
top1 = trending1.find('ul',class_='clearfix')
news=top1.find('a').text
print(news)
link=top1.find('a')['href']
print(link)
csv_writer.writerow([news,link])

#espn
source2 = requests.get('http://www.espn.in/').text

soup2 = BeautifulSoup(source2, 'lxml')

trending2=soup2.find('div',class_='headlineStack')
top2=trending2.find('ul',class_='headlineStack__list')
head=top2.find('a').text
print(head)
news_link=top2.find('a')['href']
news_link_f=f'http://www.espn.in{news_link}'
print(news_link_f)
csv_writer.writerow([head,news_link_f])

#rediff
source3 = requests.get('https://www.rediff.com/sports').text

soup3 = BeautifulSoup(source3, 'lxml')

trending3 = soup3.find('div',class_='secstorybox sports topboxheight relative')
top3 = trending3.find('h2')
link2=top3.find('a')['href']
print(link2)
headline=top3.find('a').text
print(headline)
csv_writer.writerow([headline,link])
csv_file.close()
