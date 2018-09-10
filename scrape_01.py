import requests, os, sys
from bs4 import BeautifulSoup

#get links
rss = "http://feed.zazzle.com/tjk_creative/rss?ps=100"
search =''
searchCode = 'qs='
url = "http://www.zazzle.com/tjk_creative/products?qs=&dp=252939023122309392&pg=1&ps=204"
ht= requests.get(url)

h = ht.headers
text =ht.text
soup = BeautifulSoup(text, 'html.parser')
linkList=[]
for link in soup.find_all('a'):
  linkList.append(link.get('href'))
  #print(link.get('href'))
linkSet = set(linkList)

linkList=[]
for i in linkSet:
  linkList.append(i)

post_links = []
post_title = []
for i in linkList:
  ht= requests.get(i)
  text =ht.text
  soup = BeautifulSoup(text, 'html.parser')
  post_links.append(i)
  post_title.append(soup.title.text[4:-3])
  #print("link: ",  i)
  #print("title: ", soup.title.text[4:-3])

#post_title[-3].replace(" ", " #")
# post_title[-5].split() 
