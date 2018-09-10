import requests, os, sys
from bs4 import BeautifulSoup


#lastweek
url = 'http://www.zazzle.com/gifts?st=orderitemcount_week&ps=120'
#today
url_today= 'http://www.zazzle.com/gifts?st=orderitemcount_day&ps=120&sd=desc'
# alltime
url_allTime = 'http://www.zazzle.com/gifts?st=orderitemcount_all&ps=120&sd=desc'



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
try:
    for i in linkList:
      ht= requests.get(i)
      text =ht.text
      soup = BeautifulSoup(text, 'html.parser')
      post_links.append(i)
      post_title.append(soup.title.text[4:-3])

except:
    pass


print(len(post_links))

with open( 'Store_links.txt', 'a') as f:
    i = 0
    while i <= len(post_links)-1:
        print(i)
        t = post_links[i]
        if t[-1].isnumeric():
            x = post_title[i].replace(" ", " #") + " " + post_links[i]
            x = x.replace("#| ", "")
            #todo write posts to file names 'Store_links'
            f.write("#" + x + '\n' + '\n')
            i = i + 1
        else:
            i= i + 1


#todo make defs 		
'''
with open( 'Store_links.txt', 'a') as f:
    i = 0
    try:
        while i < len(post_links):
            x = post_title[i].replace(" ", " #") + " " + post_links[i]
            x = x.replace("#| ", "")
            #todo write posts to file names 'Store_links'
            f.write(x + '\n' + '\n')
            i = i + 1    
    except:
        
        pass
'''
    
