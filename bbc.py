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
	rss_list = ['http://www.huffingtonpost.com/news/nba-finals-2013/feed/'
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
								add_to_index_file(os.getcwd() + '/' + topic + '/' + str(c) + '.txt', 'indexSport-work.txt', link, date, topic)
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


scrape('sport',1967)