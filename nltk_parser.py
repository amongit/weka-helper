import nltk
from nltk import pos_tag, word_tokenize

with open('politics_train_set_home.txt', 'r') as myfile: 
	politics = [line.decode('utf-8').strip() for line in myfile.readlines()]
	myfile.close()
nnp = 0
nns = 0
nn = 0
inn = 0
jj = 0
rb = 0
rbr = 0
rbs = 0
prp = 0
cc = 0
cd  = 0
pos_words_total = 0
count_pos_words_per_file = 0
minimum_words_per_file = 0
min_file = ''
max_file = ''
maximum_words_per_file = 0
small_list = []
medium_list = []
large_list = []
smal_list_count = 0
medium_list_count = 0
large_list_count = 0
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

	'''
# odredi broj ukupni pos tagova
# 	for tag in  tag_fd.most_common():
# 		if tag[0] == 'NN':
# 			nn += 1
# 		elif tag[0] == 'NNS':
# 			nns += 1
# 		elif tag[0] == 'NNP':
# 			nnp += 1
# 		elif tag[0] == 'IN':
# 			inn += 1
# 		elif tag[0] == 'JJ':
# 			jj += 1
# 		elif tag[0] == 'RB':
# 			rb += 1
# 		elif tag[0] == 'RBR':
# 			rbr += 1
# 		elif tag[0] == 'RBS':
# 			rbs += 1
# 		elif tag[0] == 'PRP':
# 			prp += 1
# 		elif tag[0] == 'CC':
# 			cc += 1
# 		elif tag[0] == 'CD':
# 			cd += 1
# 		else: 
# 			pos_words_total += 1
# 	print i
# print nn
# print pos_words_total

#TO DO 
#naci najmanji i najveci broj tokena u tekstu, izracunati prosecnu duzinu tekstova u vidu broja pos tagova
	for ind, tag in  enumerate(tag_fd.most_common()):
		count_pos_words_per_file += 1
	if count_pos_words_per_file > maximum_words_per_file:
		maximum_words_per_file = count_pos_words_per_file
		max_file = line
	elif count_pos_words_per_file < minimum_words_per_file:
		minimum_words_per_file = count_pos_words_per_file
		min_file = line
	if count_pos_words_per_file < 13000:
		smal_list_count += 1
		small_list.append(line)
	elif count_pos_words_per_file < 26000:
		medium_list_count += 1
		medium_list.append(line)
	else:
		large_list_count += 1
		large_list.append(line)
print minimum_words_per_file
print min_file
print maximum_words_per_file
print max_file
print 'sl'
print smal_list_count
print large_list_count
print large_list_count
print large_list

#razdvojiti u 3 kategorije od 0 do 38692