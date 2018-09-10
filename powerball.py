import requests, os, sys
from bs4 import BeautifulSoup

url_2010 ='http://www.megamillions.com/winning-numbers/search?startDate=1/1/2010&endDate=9/30/2016'
url_2011 ='http://www.megamillions.com/winning-numbers/search?startDate=1/1/2011&endDate=9/30/2016'
url_2012 ='http://www.megamillions.com/winning-numbers/search?startDate=1/1/2012&endDate=9/30/2016'
url_2013 ='http://www.megamillions.com/winning-numbers/search?startDate=1/1/2013&endDate=9/30/2016'
url_2014 ='http://www.megamillions.com/winning-numbers/search?startDate=1/1/2014&endDate=9/30/2016'
url_2015 ='http://www.megamillions.com/winning-numbers/search?startDate=1/1/2015&endDate=9/30/2016'
url_2016 ='http://www.megamillions.com/winning-numbers/search?startDate=1/1/2016&endDate=9/30/2016'


def getPage(url):
    ht= requests.get(url)
    h = ht.headers
    text =ht.text
    return BeautifulSoup(text, 'html.parser')

def myData(soup, x , y):
    # soup.find_all('td', class_="dates")
    return soup.find_all(x, class_=y)
'''
def number(soup):
    return soup.find_all('td', class_="number")

def mega(soup):
    return soup.find_all('td', class_="mega")
'''
def cleanList(data):
    l = []
    for i in data:
        l.append(i.string.strip())
    return l

def dostuff(url):

    numbers = []


    count = 0

    days = []
    for i in dates:
        days.append(i.string.strip())
        
    num = []
    for i in number:
        num.append(i.string.strip())

    meg = []
    for i in mega:
        meg.append(i.string.strip())


    temp = []
    megacount = 0
    multipliercount = 1
    minCount = 0
    maxCount = 4

    winners = []

    for i in days:
        temp = []
        temp.append(i)
        while minCount <= maxCount:
            temp.append(num[minCount])
            minCount += 1

        temp.append(meg[megacount])
        temp.append(meg[multipliercount])
        megacount+=2
        multipliercount+=2
        winners.append(temp)
        maxCount += 5


    myCount = 1
    while myCount <= 75:
        print('Total pulls for number: ' + str(myCount) , 'is ', num.count(str(myCount)))
        myCount+=1

    






if __name__ == "__main__":

    page_2010 = getPage(url_2010)
    dates = dates(page_2010, 'td',  "dates")
    
    dy = cleanList(dates)
    num = cleanList(dates)
    meg = cleanList(dates)
    #page_2011 = getPage(url_2011)
    #page_2012 = getPage(url_2012)
    #page_2013 = getPage(url_2013)
    #page_2014 = getPage(url_2014)
    #page_2015 = getPage(url_2015)
    #page_2016 = getPage(url_2016)










'''

ht= requests.get(url)
h = ht.headers
text =ht.text
soup = BeautifulSoup(text, 'html.parser')

numbers = []


dates = soup.find_all('td', class_="dates")
number =soup.find_all('td', class_="number")
mega = soup.find_all('td', class_="mega")


#day =dates[0].string.strip()
#num= number[0].string.strip()
#meg = mega[0].string.strip()


count = 0

days = []
for i in dates:
    days.append(i.string.strip())
    
num = []
for i in number:
    num.append(i.string.strip())

meg = []
for i in mega:
    meg.append(i.string.strip())


temp = []
megacount = 0
multipliercount = 1
minCount = 0
maxCount = 4

winners = []

for i in days:
    temp = []
    temp.append(i)
    while minCount <= maxCount:
        temp.append(num[minCount])
        minCount += 1

    temp.append(meg[megacount])
    temp.append(meg[multipliercount])
    megacount+=2
    multipliercount+=2
    winners.append(temp)
    maxCount += 5


myCount = 1
while myCount <= 75:
    print('Total pulls for number: ' + str(myCount) , 'is ', num.count(str(myCount)))
    myCount+=1
'''




















'''
Draw Date	Balls	Mega Ball	Megaplier	Details
8/2/2016	3	12	36	54	70	12	5	Details
8/5/2016	5	18	28	54	74	6	4	Details
8/9/2016	12	19	20	44	66	1	5	Details
8/12/2016	4	41	44	56	69	10	4	Details
8/16/2016	2	43	52	62	63	6	5	Details
8/19/2016	22	37	45	65	73	13	5	Details
8/23/2016	2	7	46	61	66	1	2	Details
8/26/2016	10	11	31	41	44	14	2	Details
8/30/2016	28	32	41	51	71	11	4	Details
9/2/2016	22	28	41	46	60	3	3	Details
9/6/2016	25	37	58	69	75	8	3	Details
9/9/2016	1	34	43	44	63	11	4	Details
9/13/2016	6	15	17	39	56	15	3	Details
9/16/2016	13	21	28	34	40	15	3	Details
'''
