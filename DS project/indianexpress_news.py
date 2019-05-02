##from bs4 import BeautifulSoup
##from urllib.request import urlopen
##import re
##
##url='https://indianexpress.com/'
##html=urlopen(url)
##soup=BeautifulSoup(html, 'lxml')
##
####top_news=soup.findAll('a',{'class':'l-grid l-grid@small---y40 l-grid@medium+--y35'})
####print(top_news)
##top_news=soup.find('div',{'class':'l-grid l-grid@small---y40 l-grid@medium+--y35'})#.findAll("a", href=re.compile(".*?"))
##
##news_link=top_news.findAll('a',{'class':'m-block-link__anchor ie-event-tacking'})
##print(news_link)
###print(top_news)
##
####for news in top_news:
####    print(news['title'], news['href'])
##


from bs4 import BeautifulSoup
import requests

res=requests.get('https://indianexpress.com/')

soup=BeautifulSoup(res.text, 'lxml')

top_news=soup.find('div',{'class':'l-grid-wrapper'})

##for t in top_news:
##    #some_news=t.find('div',{'class':'l-grid__item l-grid__item--divided one-fifth@medium'})
##    main_news=t.find('h2',{'class':'m-article-tall@medium+__title m-article-wide@small-__title'})
##    print(main_news.text)

print(top_news.text)
