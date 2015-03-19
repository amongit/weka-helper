import feedparser, urllib2, os, sys, re
reload(sys) 
sys.setdefaultencoding('utf8')
from bs4 import NavigableString 
from bs4 import BeautifulSoup 
from urllib2 import URLError, HTTPError

def scrape(topic, c = 0):
	if not os.path.exists(topic): 
		os.makedirs(topic)
	### TO DO ###
	#Include reading from list of rss feeds and maintain acurate count number
	#Read that number from the given filelist.txt
	rss_list = ['http://rss.cnn.com/rss/edition_sport.rss',
				'http://sports.yahoo.com/top/rss.xml',
				'http://sports.yahoo.com/mlb/rss.xml',
				'http://sports.yahoo.com/nfl/rss.xml',
				'http://l.yimg.com/a/i/us/ext/rss4.gif',
				'http://sports.yahoo.com/nhl/rss.xml',
				'http://sports.yahoo.com/nascar/rss.xml',
				'http://sports.yahoo.com/golf/rss.xml',
				'http://sports.yahoo.com/mma/rss.xml',
				'http://sports.yahoo.com/box/rss.xml',
				'http://sports.yahoo.com/ncaab/rss.xml',
				'http://sports.yahoo.com/ncaaw/rss.xml',
				'http://sports.yahoo.com/ten/rss.xml',
				'http://sports.yahoo.com/ncaabb/rss.xml',
				'http://sports.yahoo.com/oly/rss.xml',
				'http://sports.yahoo.com/irl/rss.xml',
				'http://sports.yahoo.com/sow/rss.xml',
				'http://sports.yahoo.com/mls/rss.xml',
				'http://sports.yahoo.com/ski/rss.xml',
				'http://sports.yahoo.com/sc/rss.xml',
				'http://www.telegraph.co.uk/sport/othersports/boxing/rss',
				'http://www.telegraph.co.uk/sport/olympics/badminton/rss',
				'http://www.telegraph.co.uk/sport/football/teams/barcelona/rss',
				'http://www.telegraph.co.uk/sport/football/teams/bosnia-and-herzegovina/rss'
				'http://www.telegraph.co.uk/sport/football/teams/brazil/rss',
				'http://www.telegraph.co.uk/sport/football/teams/serbia/rss',
				'http://www.telegraph.co.uk/sport/olympics/table-tennis/rss',
				'http://www.telegraph.co.uk/sport/motorsport/formulaone/usf1/rss',
				'http://www.telegraph.co.uk/sport/olympics/water-polo/rss',
				'http://www.telegraph.co.uk/sport/olympics/wrestling/rss',
				'http://www.telegraph.co.uk/sport/olympics/rss',
				'http://www.telegraph.co.uk/sport/tennis/novakdjokovic/rss',
				'http://www.telegraph.co.uk/sport/olympics/news/rss',
				'http://www.telegraph.co.uk/sport/football/competitions/premier-league/premier-league-clubs/rss',
				'http://www.telegraph.co.uk/sport/othersports/polo/rss',
				'http://www.telegraph.co.uk/sport/motorsport/rallying/rss',
				'http://www.telegraph.co.uk/sport/football/teams/real-madrid/rss',
				'http://www.telegraph.co.uk/sport/othersports/americanfootball/rss',
				'http://www.telegraph.co.uk/sport/football/teams/arsenal/rss',
				'http://www.telegraph.co.uk/sport/motorsport/formulaone/f1news/rss',
				'http://www.telegraph.co.uk/sport/football/competitions/euro-2012/rss',
				'http://www.telegraph.co.uk/sport/football/euro-2016/rss',
				'http://www.telegraph.co.uk/sport/football/teams/denmark/rss',
				'http://www.telegraph.co.uk/sport/olympics/cycling/rss',
				'http://www.telegraph.co.uk/sport/cricket/rss',
				'http://www.telegraph.co.uk/sport/olympics/football/rss',
				'http://www.telegraph.co.uk/sport/football/teams/france/rss',
				'http://www.telegraph.co.uk/sport/rugbyunion/international/france/rss',
				'http://www.telegraph.co.uk/sport/motorsport/formulaone/rss',
				'http://www.telegraph.co.uk/sport/football/footballfive/rss',
				'http://www.telegraph.co.uk/sport/olympics/gymnastics/rss',
				'http://www.telegraph.co.uk/sport/othersports/icehockey/rss',
				'http://www.telegraph.co.uk/sport/olympics/judo/rss',
				'http://www.telegraph.co.uk/sport/othersports/lacrosse/rss',
				'http://www.telegraph.co.uk/sport/rugbyunion/international/newzealand/rss',
				'http://www.telegraph.co.uk/sport/rugbyunion/international/newzealand/rss',
				'http://www.telegraph.co.uk/sport/rugbyunion/news/rss',
				'http://www.telegraph.co.uk/sport/olympics/sailing/rss',
				'http://www.telegraph.co.uk/sport/football/teams/slovakia/rss',
				'http://www.telegraph.co.uk/sport/football/teams/spain/rss',
				'http://www.telegraph.co.uk/sport/sportvideo/sport-explained/rss',
				'http://www.telegraph.co.uk/sport/sports-personality-of-the-year/rss',
				'http://www.telegraph.co.uk/sport/football/teams/switzerland/rss',
				'http://www.telegraph.co.uk/sport/othersports/cycling/tour-de-france/rss',
				'http://www.telegraph.co.uk/sport/othersports/cycling/track-cycling/rss',
				'http://www.telegraph.co.uk/sport/othersports/ufc/rss',
				'http://www.telegraph.co.uk/sport/othersports/sailing/volvo-ocean-race/rss',
				'http://www.telegraph.co.uk/sport/olympics/volleyball/rss',
				'http://www.telegraph.co.uk/sport/tennis/wtatour/rss',
				'http://www.telegraph.co.uk/sport/football/world-cup/rss',
				'http://www.telegraph.co.uk/sport/tennis/williamssisters/rss',
				'http://www.telegraph.co.uk/sport/olympics/weightlifting/rss',
				'http://www.telegraph.co.uk/sport/golf/usopen/rss',
				'http://www.telegraph.co.uk/sport/othersports/surfing/rss',
				'http://www.telegraph.co.uk/sport/tennis/rafaelnadal/rss',
				'http://www.telegraph.co.uk/sport/olympics/modern-pentathlon/rss',
				'http://www.telegraph.co.uk/sport/othersports/athletics/london-marathon/rss',
				'http://www.telegraph.co.uk/sport/football/players/landon-donovan/rss',
				'http://www.telegraph.co.uk/sport/football/teams/manchester-city/rss',
				'http://www.telegraph.co.uk/sport/football/teams/mexico/rss',
				'http://www.telegraph.co.uk/sport/mysport/rss',
				'http://www.telegraph.co.uk/sport/columnists/matt-law/rss',
				'http://www.telegraph.co.uk/sport/olympics/mobile-guides/rss',
				'http://www.telegraph.co.uk/sport/football/teams/manchester-united/rss',
				'http://preview.telegraph.co.uk/sport/columnists/james-anderson/rss',
				'http://www.telegraph.co.uk/sport/columnists/jacquelin-magnay/rss',
				'http://www.telegraph.co.uk/sport/football/european/rss',
				'http://www.telegraph.co.uk/sport/golf/europeantour/rss',
				'http://www.telegraph.co.uk/sport/football/teams/exeter-city/rss',
				'http://www.telegraph.co.uk/sport/rugbyunion/european-rugby/rss',
				'http://www.telegraph.co.uk/sport/tennis/daviscup/rss',
				'http://www.telegraph.co.uk/sport/cricket/cricket-world-cup/rss'
				'http://feeds.reuters.com/reuters/sportsNews',
				'http://feeds.bbci.co.uk/sport/0/football/rss.xml?edition=uk',
				'http://feeds.bbci.co.uk/sport/0/tennis/rss.xml?edition=uk',
				'http://feeds.bbci.co.uk/sport/0/cricket/rss.xml?edition=uk',
				'http://feeds.bbci.co.uk/sport/0/rugby-union/rss.xml?edition=uk',
				'http://feeds.bbci.co.uk/sport/0/rugby-league/rss.xml?edition=uk',
				'http://newsrss.bbc.co.uk/rss/sportplayer_uk_edition/golf/rss.xml',
				'http://newsrss.bbc.co.uk/rss/sportplayer_uk_edition/motorsport/rss.xml',
				'http://newsrss.bbc.co.uk/rss/sportplayer_uk_edition/boxing/rss.xml',
				'http://newsrss.bbc.co.uk/rss/sportplayer_uk_edition/athletics/rss.xml',
				'http://newsrss.bbc.co.uk/rss/sportplayer_uk_edition/snooker/rss.xml',
				'http://www.huffingtonpost.com/feeds/verticals/sports/index.xml',
				'http://www.huffingtonpost.com/news/combat-sports/feed/',
				'http://www.huffingtonpost.com/news/detroit-sports/feed/',
				'http://www.huffingtonpost.com/news/fox-sports-1/feed/',
				'http://www.huffingtonpost.com/news/religion-and-sports/feed/',
				'http://www.huffingtonpost.com/news/impact-sports/feed/',
				'http://www.huffingtonpost.com/news/miami-sports/feed/'
				'http://www.huffingtonpost.com/news/sports-fails/feed/',
				'http://www.huffingtonpost.com/news/science-of-sport/feed/',
				'http://www.huffingtonpost.com/news/motorsports/feed/',
				'http://www.huffingtonpost.com/news/basketball/feed/',
				'http://www.huffingtonpost.com/news/big-ten-football/feed/'
				'http://www.huffingtonpost.com/news/baseball/feed/',
				'http://www.huffingtonpost.com/news/football/feed/',
				'http://www.huffingtonpost.com/news/football-foods/feed/',
				'http://www.huffingtonpost.com/news/olympic-basketball/feed/',
				'http://www.huffingtonpost.com/news/olympic-gymnastics/feed/',
				'http://www.huffingtonpost.com/news/olympic-glory/feed/',
				'http://www.huffingtonpost.com/news/olympic-soccer/feed/',
				'http://www.huffingtonpost.com/news/olympics/feed/',
				'http://www.huffingtonpost.com/news/tennis/feed/'
				]
			
	for rss_url in rss_list:
		try:
			d = feedparser.parse(rss_url)

			text = '' # contains link, title and article body
			body = ''
			if d.entries:
				for i in range(0, len(d.entries)):
					if d.entries[i]['link'] != '':
						link = d.entries[i]['link'] 
						date = d.entries[i]['published'] 

						htmlfile = urllib2.urlopen(link)
						htmltext = htmlfile.read() 
						soup = BeautifulSoup(htmltext) 
						if soup.h1.string and link.find('nationaljournal') == -1:
							title = soup.h1.string
						else:
							title = soup.title.string

						article_body = ''
						print link
						print title
						#break

						text += remove_new_line(link) + '\n'
						text += remove_new_line(title) + '\n'
						try :
							# ToDo write switch if url contains washingtonpost than p_list ...
							# default: most used case with

							# For Waashington post 			p_list = soup.find_all('article')
							#'''For zdnet, bbc, techrepublic

							#p_list = soup.find("div", {"class": ["article", 'emp-decription',
							#'story-body','content','l-container', 'storyBody', 'column1','p402_premium','body', 'story', 
							#'zn-body__paragraph', 'cnnContentContainer']}).find_all('p')

							#p_list = soup.find("div", {"id": ["mainBodyArea"]}).find_all('p')
							# print p_list
							# break

							#For CNN
							if link.find('cnn') != -1:
								p_list = soup.find_all("p", {'class': ['zn-body__paragraph', 'cnnContentContainer']}) #CNN
							elif link.find('washingtonpost') != -1:
								p_list = soup.find_all('article')
							elif link.find('cbc') != -1:
								p_list = soup.find("div", {'class': ['story-content']}).find_all('p')
							elif link.find('thenation') != -1:
								p_list = soup.find('div', {'class' : ['blog-body']}).find_all('p')
							elif link.find('ibnlive') != -1:
								p_list = soup.find('article', {'class' : ['article_cbox']}).find_all('p')
							elif link.find('huffingtonpost') != -1:
								p_list = soup.find('div', {'id': 'mainentrycontent'}).find_all('p')

							# elif link.find('nationaljournal') != -1:
							# 	p_list = soup.find('id', {'class': ['articleBodyContent']})
							
							else:
								p_list = soup.find('div', {'class': ['magWYSIWYG','WYSIWYG', 'article','emp-decription',
								'story-body','content','l-container', 'storyBody', 'column1','p402_premium','body', 'story', 
								'zn-body__paragraph', 'cnnContentContainer','storytext','g_2', 'storyTextMd', 'block']}).find_all('p')
							
							#Iterates through three levels of p tag and checking wether it contains string or another tags
							for index, p_tag in enumerate(p_list):
								for i in range(0, len(p_tag.contents)):
									if isinstance(p_tag.contents[i], NavigableString) and not p_tag.contents[i].find("Read more") == 0 and not p_tag.contents[i].find("Read:") == 0 and not p_tag.contents[i].find("Follow us") == 0:
										body += p_tag.contents[i]
									else:
										for j in range(0, len(p_tag.contents[i])):
											if isinstance(p_tag.contents[i].contents[j], NavigableString):
												body += p_tag.contents[i].contents[j]
											else:
												for k in range(0, len(p_tag.contents[i].contents[j])):
													if isinstance(p_tag.contents[i].contents[j].contents[k], NavigableString):
														body += p_tag.contents[i].contents[j].contents[k]
													else:
														print 'Something unparsable  .......\n'
														print p_tag.contents[i].contents[j].contents[k].get_text()
														print '.................................\n\n\n\n'

								
								article_body += remove_new_line(body)
								article_body += '\n'
								body = ''
	
							#text += remove_new_line(body) ove dve linije ako ne zelim paragrafe razdvojene '\n'
							#print text

							text += article_body
							print text
							if(article_body):
								add_to_index_file(os.getcwd() + '/' + topic + '/' + str(c) + '.txt', 'indexSport.txt', link, date, topic)
								with open(topic + '/' + str(c) + '.txt', 'w') as myfile: 
									myfile.write(text.encode("utf-8")) 
									myfile.close()
								
								c += 1
								text = ''
								# body = ''-
								# if c == 1:
								# 	break 
						except:
							pass
		except:
			pass

def add_to_index_file(count, file_name, link, date, topic):
	with open(file_name, 'a') as myfile: 
		myfile.write(str(count) + '\t' + link + '\t' + date + '\t' + topic + '\n') 
	myfile.close()

def remove_new_line(text):
	return ' '.join(text.split())


scrape('sport',0)