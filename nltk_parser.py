import nltk
from nltk import pos_tag, word_tokenize

with open('politics_train_set.txt', 'r') as myfile: 
	politics = [line.decode('utf-8').strip() for line in myfile.readlines()]
	myfile.close()

text = []
tagged_text = []
for i, line in enumerate(politics):
	with open(line, 'r') as myfile: 
		whole_text = myfile.read().decode('utf-8')
		myfile.close()
	text_tokenized = word_tokenize(whole_text)
	text_pos_tagged = nltk.pos_tag(text_tokenized)
	tag_fd = nltk.FreqDist(tag for (word, tag) in text_pos_tagged)
	''' najcesca vrsta reci pre imenice 
	word_tag_pairs = nltk.bigrams(text_pos_tagged)
	noun_preceders = [a[1] for (a, b) in word_tag_pairs if b[1] == 'NN'] 
	fdist = nltk.FreqDist(noun_preceders)
	print [tag for (tag, _) in fdist.most_common()]
	'''

	#print text_tagged
	tag_fd = nltk.FreqDist(tag for (word, tag) in text_tagged)
	print tag_fd.plot(cumulative=True)

	'''' glagoli poredjani po ucestalosti u tekstu'''
	[wt[0] for (wt, _) in tag_fd.most_common() if wt[1] == 'VBD']
	#vraca najcestiji pos
	#print tag_fd.most_common()[0][1]
	break

