import pandas as pd

columns = ['headline','News_link']
df = pd.read_csv('sports.csv', names=columns)
f=open("newtext2.html","w")
f.write(df.to_html())
link=[]
head=[]
for x in df['News_link']:
    link.append(x)
for x in df['headline']:
    head.append(x)
def form(head_line,newslink):
    return '<td><a href="{}">{}</a></td>'.format(newslink,head_line)

new=[]
for i in range(0,len(link)):
    new.append(form(head[i],link[i]))
f.close()
file=open("newtext2.html","r+")
m=[]
c=0
for i in file:
    m.append(i)
    c=c+1

var=12
for i in new:
    m[var]=i
    var=var+5
dele=11
for i in new:    
    m.pop(dele)
    dele=dele+4
m.pop(5)

for i in m:
    file.write(i)

file.close()

fi=open("newtext3.html","w")
for i in m:
    fi.write(i)
fi.close()







    
