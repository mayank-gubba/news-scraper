from bs4 import BeautifulSoup
import requests

res=requests.get('https://inshorts.com/en/read')

soup=BeautifulSoup(res.text, 'lxml')

headlines=soup.find('a',{'class':'clickable'})
print(headlines.text)
