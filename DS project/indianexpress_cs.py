from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://indianexpress.com/').text

soup = BeautifulSoup(source, 'lxml')

trend=soup.find('div',class_='l-grid-wrapper')

part=trend.find('div',class_='l-grid__item l-grid__item--divided one-fifth@medium')

##headline=part.a.text
##print(headline)

##link=part.find('a',class_='m-block-link__anchor ie-event-tacking')['href']
##print(link)

footer=part.find('div',class_='m-article__footer')
##author=footer.a.text
##print(author)

timing=footer.time.text
print(timing)
print()
