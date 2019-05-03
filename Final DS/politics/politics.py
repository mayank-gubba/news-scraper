from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.news18.com/politics/').text

csv_file= open('politics.csv','w')
csv_writer=csv.writer(csv_file)

soup = BeautifulSoup(source, 'lxml')

#link1

trending1=soup.find('div', class_='section-blog-left-img-list')
topic1 = trending1.find('ul')
top1=topic1.find('li')

headline=top1.find('a').text
print(headline)
link=top1.find('a')['href']
print(link)
csv_writer.writerow([headline,link])
#link2

trending2=soup.find('div',class_='blog-list')
topic2=trending2.find('div',class_='blog-list-blog')

side=topic2.find('p')

head2=side.find('a')['href']
print(head2)
link2=side.find('a').text
print(link2)
csv_writer.writerow([head2,link2])
#link3

source2 = requests.get('https://www.foxnews.com/politics').text

soup2 = BeautifulSoup(source2,'lxml')

trending3=soup2.find('div',class_='siderbar-columns')

top3=trending3.find('div',class_='content article-list')

side3=top3.find('div',class_='info')

main3=side3.find('h4',class_='title')

head3=main3.find('a').text
print(head3)
link3=main3.find('a')['href']
flink=f'https://www.foxnews.com{link3}'
print(flink)
csv_writer.writerow([head3,flink])

csv_file.close()
