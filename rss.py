#http://feeds.bbci.co.uk/sport/0/football/rss.xml?edition=uk
#http://feeds.bbci.co.uk/sport/0/tennis/rss.xml?edition=uk
#http://feeds.bbci.co.uk/sport/0/cricket/rss.xml?edition=uk
#http://feeds.bbci.co.uk/sport/0/rugby-union/rss.xml?edition=uk
#http://feeds.bbci.co.uk/sport/0/rugby-league/rss.xml?edition=uk
#http://newsrss.bbc.co.uk/rss/sportplayer_uk_edition/golf/rss.xml
#http://newsrss.bbc.co.uk/rss/sportplayer_uk_edition/motorsport/rss.xml
#http://newsrss.bbc.co.uk/rss/sportplayer_uk_edition/boxing/rss.xml
#http://newsrss.bbc.co.uk/rss/sportplayer_uk_edition/athletics/rss.xml
#http://newsrss.bbc.co.uk/rss/sportplayer_uk_edition/snooker/rss.xml
#http://feeds.bbci.co.uk/news/politics/rss.xml

#http://feeds.bbci.co.uk/news/technology/rss.xml?edition=uk
def scrape(topic):
	import feedparser, urllib2, os, sys, re
	reload(sys) 
	sys.setdefaultencoding('utf8') 
	from bs4 import BeautifulSoup 
	from urllib2 import URLError, HTTPError
	d = feedparser.parse('http://rss.cnn.com/rss/edition_technology.rss')
	if not os.path.exists(topic): 
		os.makedirs(topic)
	c = 35
	text = '' 
	for i in range(0, len(d.entries)):
		print d.entries[i]['link']
		htmlfile = urllib2.urlopen(d.entries[i]['link'])
		htmltext = htmlfile.read() 
		soup = BeautifulSoup(htmltext) 
		title = soup.title.string

		text += d.entries[i]['link'] + '\n'
		text += title + '\n'
		try :
			article_box = soup.find("div", {"class": ["article", 'emp-decription','story-body','content','l-container']}).find_all('p')
			# finds container div which holds all paragraphs with the story content
			print article_box
			# iterates through those p elements some of them contain a tag
			for para in article_box:
				if para.string == None:
					# if para.string is not just plain paragraph containing text
					# it has to be iterated again to get to the value of anchor tag
					for k in para.contents:
						print k.string
						text += str(k.string) + '\n'
				else:
					print para.string
					text += para.string + '\n'
			print text
			with open('list.txt', 'a') as myfile: 
				myfile.write(str(c) + '\t' + d.entries[i]['link'] + '\t' + topic + '\n') 
			with open(topic + '/' + str(c) + '.txt', 'w') as myfile: 
				myfile.write(text.encode("utf-8")) 
			c += 1
			text = '' 
		except:
			pass

scrape('technology')