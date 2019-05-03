from bs4 import BeautifulSoup
import requests
import csv

source1 = requests.get('https://www.ndtv.com/entertainment').text

csv_file= open('entertain.csv','w')
csv_writer=csv.writer(csv_file)
#link1
soup1 = BeautifulSoup(source1, 'lxml')

trending1=soup1.find('div',class_='new_storylising')

top1=trending1.find('li')

story=top1.find('div',class_='nstory_header')

head1=story.find('a').text
print(head1)
link1=story.find('a')['href']
print(link1)

csv_writer.writerow([head1,link1])

#link2
source2 = requests.get('https://timesofindia.indiatimes.com/entertainment').text

soup2 = BeautifulSoup(source2, 'lxml')

trending2=soup2.find('div',class_='lftbig_txt')

link2=trending2.find('a')['href']
flink2=f'https://www.indiatoday.in{link2}'
print(flink2)
head2=trending2.find('a').h3.text
print(head2)
csv_writer.writerow([head2,flink2])

#link3
trending3=soup2.find('div',class_='small_video_lft chng_lfttxt')

head3=trending3.find('a')['alt']
print(head3)
link3=trending3.find('a')['href']
flink3=f'https://www.indiatoday.in{link3}'
print(flink3)

csv_writer.writerow([head3,flink3])

csv_file.close()
