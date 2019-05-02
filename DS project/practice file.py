from newspaper import Article 
  
#A new article from TOI 
url = "https://indianexpress.com/"
  
#For different language newspaper refer above table 
toi_article = Article(url, language="en") # en for English 
  
#To download the article 
toi_article.download() 
  
#To parse the article 
toi_article.parse() 
  
#To perform natural language processing ie..nlp 
#toi_article.nlp() 
  
#To extract title 
print("Article's Title:") 
print(toi_article.title) 
print("n") 
