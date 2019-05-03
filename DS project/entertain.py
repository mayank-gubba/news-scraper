from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.hindustantimes.com/entertainment/').text

csv_file= open('entertain.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','news_link'])

soup = BeautifulSoup(source, 'lxml')

trending=soup.find('div',class_='banner-thumbs')

top = trending.find('ul',class_='clearfix')

news1=top.find('a',id='1').text
print(news1)
link1=top.find('a',id='1')['href']
print(link1)
csv_writer.writerow([news1,link1])

news2=top.find('a',id='2').text
print(news2)
link2=top.find('a',id='2')['href']
print(link2)
csv_writer.writerow([news2,link2])

news3=top.find('a',id='3').text
print(news3)
link3=top.find('a',id='3')['href']
print(link3)
csv_writer.writerow([news3,link3])

csv_file.close()
