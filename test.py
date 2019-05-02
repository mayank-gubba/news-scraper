import pandas as pd

columns = ['headline','News_link']
df = pd.read_csv('indiatoday.csv', names=columns)
f=open("newtext.html","w")
f.write(df.to_html())
f.close()
