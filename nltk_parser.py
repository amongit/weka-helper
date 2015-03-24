import nltk
from nltk import pos_tag, word_tokenize
with open('politics_train_set.txt', 'r') as myfile: 
	politics = [line.decode('utf-8').strip() for line in myfile.readlines()]
	print politics
	myfile.close()
	#politics_list = politics.split('\n')

for line in politics:
	with open(line, 'r') as myfile: 
		whole_text = myfile.read().decode('utf-8')
		myfile.close()

	# text = nltk.Text(word.lower() for word in whole_text)
	text = word_tokenize(whole_text)

	text_tagged = nltk.pos_tag(text)
	#print text_tagged
	tag_fd = nltk.FreqDist(tag for (word, tag) in text_tagged)
	print tag_fd.plot(cumulative=True)