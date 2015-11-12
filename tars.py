import requests 
from bs4 import BeautifulSoup
def crawl(l):
	f = requests.get(l)
	data = f.text
	soup = BeautifulSoup(data,'lxml')
	links = soup.find_all('li',{'class':'grid-full mb-30'})
	for x in links:
		title = x.find('div',{'class':'title-small bentonCondensed bold color-black-2 truncate-2'})
		title = title.text.strip().encode('utf8')
		print title
		#IMPORTANT PLEASE READ
		#Uncomment the Next 4 Lines if you want the Titles to be stored in a Text File.
		#fo = open('title.txt','a')
		#fo.write(title)
		#fo.write('\n')	
		#fo.close()
	try:
		nextl = soup.find('a',{'class':'bentonCondensed uc color-red pagesNav-nextPage phn-fl'})['href']
		crawl(nextl)
	except:
		print "End of Stories"

crawl('http://yourstory.com/ys-stories')
del crawl