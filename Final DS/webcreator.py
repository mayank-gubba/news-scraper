import pandas as pd

##1
columns = ['headline','News_link']
df = pd.read_csv('trending.csv', names=columns)
f=open("sample1.html","w")
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
file=open("sample1.html","r+")
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
m[3]="<th>S.no</th>"
m[4]="<th align=center>Trending</th>"
m[9]="<td>1</td>"
m[13]="<td>2</td>"
m[17]="<td>3</td>"
m[21]="<td>4</td>"
m[25]="<td>5</td>"
fi=open("News.html","w")
for i in m:
    fi.write(i)
fi.close()


#2

columns1 = ['headline','News_link']
df1 = pd.read_csv('entertain.csv', names=columns1)
f1=open("sample2.html","w")
f1.write(df1.to_html())
link1=[]
head1=[]
for x in df1['News_link']:
    link1.append(x)
for x in df1['headline']:
    head1.append(x)
def form(head_line,newslink):
    return '<td><a href="{}">{}</a></td>'.format(newslink,head_line)

new1=[]
for i in range(0,len(link1)):
    new1.append(form(head1[i],link1[i]))
f1.close()
file1=open("sample2.html","r+")
m1=[]
c1=0
for i in file1:
    m1.append(i)
    c1=c1+1

var1=12
for i in new1:
    m1[var1]=i
    var1=var1+5
dele1=11
for i in new1:    
    m1.pop(dele1)
    dele1=dele1+4
m1.pop(5)

for i in m1:
    file1.write(i)

file1.close()
m1[3]="<th>S.no</th>"
m1[4]="<th align=center>Entertainment</th>"
m1[9]="<td>1</td>"
m1[13]="<td>2</td>"
m1[17]="<td>3</td>"

fi1=open("News.html","a")
for i in m1:
    fi1.write(i)
fi1.close()


#3


columns2 = ['headline','News_link']
df2 = pd.read_csv('sports.csv', names=columns2)
f2=open("sample3.html","w")
f2.write(df2.to_html())
link2=[]
head2=[]
for x in df2['News_link']:
    link2.append(x)
for x in df2['headline']:
    head2.append(x)
def form(head_line,newslink):
    return '<td><a href="{}">{}</a></td>'.format(newslink,head_line)

new2=[]
for i in range(0,len(link2)):
    new2.append(form(head2[i],link2[i]))
f2.close()
file2=open("sample3.html","r+")
m2=[]
c2=0
for i in file2:
    m2.append(i)
    c2=c2+1

var2=12
for i in new2:
    m2[var2]=i
    var2=var2+5
dele2=11
for i in new2:    
    m2.pop(dele2)
    dele2=dele2+4
m2.pop(5)

for i in m2:
    file2.write(i)

file2.close()
m2[3]="<th>S.no</th>"
m2[4]="<th align=center>Sports</th>"
m2[9]="<td>1</td>"
m2[13]="<td>2</td>"
m2[17]="<td>3</td>"
fi2=open("News.html","a")
for i in m2:
    fi2.write(i)
fi2.close()


#4

columns3 = ['headline','News_link']
df3 = pd.read_csv('politics.csv', names=columns3)
f3=open("sample4.html","w")
f3.write(df3.to_html())
link3=[]
head3=[]
for x in df3['News_link']:
    link3.append(x)
for x in df3['headline']:
    head3.append(x)
def form(head_line,newslink):
    return '<td><a href="{}">{}</a></td>'.format(newslink,head_line)

new3=[]
for i in range(0,len(link3)):
    new3.append(form(head3[i],link3[i]))
f3.close()
file3=open("sample4.html","r+")
m3=[]
c3=0
for i in file3:
    m3.append(i)
    c3=c3+1

var3=12
for i in new3:
    m3[var3]=i
    var3=var3+5
dele3=11
for i in new3:    
    m3.pop(dele3)
    dele3=dele3+4
m3.pop(5)

for i in m3:
    file3.write(i)

file3.close()
m3[3]="<th>S.no</th>"
m3[4]="<th align=center>Politics</th>"
m3[9]="<td>1</td>"
m3[13]="<td>2</td>"
m3[17]="<td>3</td>"

fi3=open("News.html","a")
for i in m3:
    fi3.write(i)
fi3.close()

