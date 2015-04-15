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
		rss_list = ['http://feeds.bbci.co.uk/news/technology/rss.xml?edition=uk',
				'http://techrepublic.com.feedsportal.com/c/35463/f/670841/index.rss',
				'http://www.zdnet.com/blog/transforming-datacenter/rss.xml',
				'http://www.zdnet.com/blog/smb-india/rss.xml',
				'http://www.zdnet.com/blog/indonesia-biztech/rss.xml',
				'http://www.zdnet.com/blog/hong-kong-techie/rss.xml',
				'http://www.zdnet.com/blog/tech-taiwan/rss.xml',
				'http://www.zdnet.com/blog/startup-india/rss.xml',
				'http://www.zdnet.com/blog/starting-up-asia/rss.xml',
				'http://www.zdnet.com/blog/partner/rss.xml',
				'http://www.zdnet.com/blog/post-pc/rss.xml',
				'http://www.zdnet.com/blog/benelux/rss.xml',
				'http://www.zdnet.com/blog/heat-sink/rss.xml',
				'http://www.zdnet.com/blog/italy/rss.xml',
				'http://www.zdnet.com/blog/african-enterprise/rss.xml',
				'http://www.zdnet.com/blog/new-india/rss.xml',
				'http://www.zdnet.com/blog/estonia/rss.xml',
				'http://www.zdnet.com/blog/iberia/rss.xml',
				'http://www.zdnet.com/blog/brazil/rss.xml',
				'http://www.zdnet.com/blog/500-words-into-the-future/rss.xml',
				'http://www.zdnet.com/blog/sap/rss.xml',
				'http://www.zdnet.com/blog/microsoft/rss.xml', 
				'http://www.zdnet.com/blog/back-office/rss.xml',
				'http://www.zdnet.com/blog/barker-bites-back/rss.xml',
				'http://www.zdnet.com/blog/btl/rss.xml',
				'http://www.zdnet.com/blog/big-data/rss.xml',
				'http://www.zdnet.com/blog/bootstrappr/rss.xml',
				'http://www.zdnet.com/blog/by-the-way/rss.xml',
				'http://www.zdnet.com/blog/central-europe/rss.xml',
				'http://www.zdnet.com/blog/cloud-builders/rss.xml',
				'http://www.zdnet.com/blog/communication-breakdown/rss.xml',
				'http://www.zdnet.com/blog/collaboration/rss.xml',
				'http://www.zdnet.com/blog/constellation/rss.xml',
				'http://www.zdnet.com/blog/consumerization/rss.xml',
				'http://www.zdnet.com/blog/diy-it/rss.xml',
				'http://www.zdnet.com/blog/hinchcliffe/rss.xml',
				'http://www.zdnet.com/blog/datacenter/rss.xml',
				'http://www.zdnet.com/blog/forrester/rss.xml',
				'http://www.zdnet.com/blog/full-duplex/rss.xml',
				'http://www.zdnet.com/blog/gen-why/rss.xml',
				'http://www.zdnet.com/blog/hardware/rss.xml',
				'http://www.zdnet.com/blog/identity/rss.xml',
				'http://www.zdnet.com/blog/igeneration/rss.xml',
				'http://www.zdnet.com/blog/cisco/rss.xml',
				'http://www.zdnet.com/blog/projectfailures/rss.xml',
				'http://www.zdnet.com/blog/jamies-mostly-linux-stuff/rss.xml',
				'http://www.zdnet.com/blog/jacks-blog/rss.xml',
				'http://www.zdnet.com/blog/computers/rss.xml',
				'http://www.zdnet.com/blog/open-source/rss.xml',
				'http://www.zdnet.com/blog/london/rss.xml',
				'http://www.zdnet.com/blog/mapping-babel/rss.xml',
				'http://www.zdnet.com/blog/mixed-signals/rss.xml',
				'http://www.zdnet.com/blog/mobile-india/rss.xml',
				'http://www.zdnet.com/blog/mobile-news/rss.xml',
				'http://www.zdnet.com/blog/networking/rss.xml',
				'http://www.zdnet.com/blog/norse-code/rss.xml',
				'http://www.zdnet.com/blog/null-pointer/rss.xml',
				'http://www.zdnet.com/blog/the-full-tilt/rss.xml',
				'http://www.zdnet.com/blog/pinoy-post/rss.xml',
				'http://www.zdnet.com/blog/practically-tech/rss.xml',
				'http://www.zdnet.com/blog/product-central/rss.xml',
				'http://www.zdnet.com/blog/violetblue/rss.xml',
				'http://www.zdnet.com/blog/qubits-and-pieces/rss.xml',
				'http://www.zdnet.com/blog/securify-this/rss.xml',
				'http://www.zdnet.com/blog/service-oriented/rss.xml',
				'http://www.zdnet.com/blog/small-talk/rss.xml',
				'http://www.zdnet.com/blog/small-business-matters/rss.xml',
				'http://www.zdnet.com/blog/cell-phones/rss.xml',
				'http://www.zdnet.com/topic/android/rss.xml',
				'http://www.zdnet.com/topic/apple/rss.xml',
				'http://www.zdnet.com/topic/browser/rss.xml',
				'http://www.zdnet.com/topic/collaboration/rss.xml',
				'http://www.zdnet.com/topic/enterprise-software/rss.xml',
				'http://www.zdnet.com/topic/google/rss.xml',
				'http://www.zdnet.com/topic/great-debate/rss.xml',
				'http://www.zdnet.com/topic/hardware/rss.xml',
				'http://www.zdnet.com/topic/ibm/rss.xml',
				'http://www.zdnet.com/topic/ios/rss.xml',
				'http://www.zdnet.com/topic/iphone/rss.xml',
				'http://www.zdnet.com/topic/ipad/rss.xml',
				'http://www.zdnet.com/topic/it-priorities/rss.xml',
				'http://www.zdnet.com/topic/laptops/rss.xml',
				'http://www.zdnet.com/topic/legal/rss.xml',
				'http://www.zdnet.com/topic/linux/rss.xml',
				'http://www.zdnet.com/topic/microsoft/rss.xml',
				'http://www.zdnet.com/topic/mobile-os/rss.xml',
				'http://www.zdnet.com/topic/mobility/rss.xml',
				'http://www.zdnet.com/topic/networking/rss.xml',
				'http://www.zdnet.com/topic/operating-systems/rss.xml',
				'http://www.zdnet.com/topic/oracle/rss.xml',
				'http://www.zdnet.com/topic/processors/rss.xml',
				'http://www.zdnet.com/topic/samsung/rss.xml',
				'http://www.zdnet.com/topic/security/rss.xml',
				'http://www.zdnet.com/blog/feeds/rss.xml',
				'http://www.zdnet.com/blog/crm/rss.xml',
				'http://www.zdnet.com/blog/sommer/rss.xml',
				'http://www.zdnet.com/blog/storage/rss.xml',
				'http://www.zdnet.com/blog/apac-redhat/rss.xml',
				'http://www.zdnet.com/blog/techie-isles/rss.xml',
				'http://www.zdnet.com/blog/technolatte/rss.xml'
				'http://www.zdnet.com/blog/tech-podium/rss.xml'
				'http://www.huffingtonpost.com/news/education-technology/feed/',
				'http://www.huffingtonpost.com/news/green-technology/feed/',
				'http://www.huffingtonpost.com/feeds/verticals/technology/index.xml',
				'http://www.huffingtonpost.com/news/bill-gates/feed/',
				'http://www.huffingtonpost.com/news/computer-science/feed/'
				'http://www.huffingtonpost.com/news/computers/feed/'
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
								add_to_index_file(os.getcwd() + '/' + topic + '/' + str(c) + '.txt', 'indexTechnology2-work.txt', link, date, topic)
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


scrape('technology2',0)