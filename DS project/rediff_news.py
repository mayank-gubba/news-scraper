from bs4 import BeautifulSoup
import requests

res=requests.get('https://www.rediff.com/news')

soup=BeautifulSoup(res.text, 'lxml')

news_box=soup.find('div',{'class':'secstorybox'})

print(news_box.text)
