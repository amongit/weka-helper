#http://rss.cnn.com/rss/edition_technology.rss
#http://rss.cnn.com/rss/edition_sport.rss
#http://rss.cnn.com/rss/edition_space.rss
def scrape(topic, count):
	import feedparser, urllib2, os, sys
	reload(sys) 
	sys.setdefaultencoding('utf8') 
	from bs4 import BeautifulSoup 
	from urllib2 import URLError, HTTPError
	d = feedparser.parse('http://rss.cnn.com/rss/edition_sport.rss')
	if not os.path.exists(topic): 
		os.makedirs(topic)
	text = '' 
	if not os.path.exists('sport'): 
		os.makedirs('sport')
	for entry in d.entries:
		print entry['link']
		print d.entries
		break
		htmlfile = urllib2.urlopen(entry['link'])
		htmltext = htmlfile.read() 
		soup = BeautifulSoup(htmltext) 

		article_text = soup.find_all(attrs={'class': ['zn-body__paragraph', 'cnnContentContainer']})
		
		for a in article_text:
			if a.string != '':
				print a.contents
				for l in a.contents:
					if str(l.string) != '':
						text += str(l.string) + '\n' #u'\u0020'

		with open(topic + '/' + str(count) + '.txt', 'w') as myfile: 
			myfile.write(text.encode("utf-8")) 
			print text
		with open('list.txt', 'a') as myfile: 
			myfile.write(str(count) + '\t' + entry['link'] + '\t' + topic + '\n') 
		count += 1
		text = '' 

scrape('test', 0)

	
	

