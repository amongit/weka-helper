import nltk, json
from nltk import pos_tag, word_tokenize


def read_list_of_files(input_text):
	with open(input_text, 'r') as myfile: 
		path_list = [line.decode('utf-8').strip() for line in myfile.readlines()]
		myfile.close()
	return path_list

def get_file_list(input_file):
	with open(input_file, 'r') as myfile: 
		file_list = [line.decode('utf-8').strip() for line in myfile.readlines()]
		myfile.close()
	return file_list

def pos_tag_analysis(file_list, report_file):
	#TO DO napraviti algorithmia input lista sa nizom fajlova output json sa tagovima i statistikama
	cc = cd = dt = ex = fw = inn = jj = jjr = jjs\
	 = ls = md = nn = nns = nnp = nnps = pdt = pos \
	 = prp = prps = rb = rbr = rbs = rp = sym = to = uh \
	 = vb = vbd = vbg = vbn = vbp = vbz = wdt = wp = wps = wrb = pos_tags_total = 0
	for li, line in enumerate(file_list):
		with open(line, 'r') as myfile: 
			whole_text = myfile.read().decode('utf-8')
			myfile.close()
		text_tokenized = word_tokenize(whole_text)
		text_pos_tagged = nltk.pos_tag(text_tokenized)
		tag_fd = nltk.FreqDist(tag for (word, tag) in text_pos_tagged)


		# tags = ['cc', 'cd', 'dt', 'ex', 'fw', 'in', 'jj', 'jjr', 'jjs', 'ls', 'md', 'nn', 'nns', 'nnp', 'nnps', 'pdt', 'pos', 'prp', '\
		# prp$', 'rb', 'rbr', 'rbs', 'rp', 'sym', 'to', 'uh', 'vb', 'vbd', 'vbg', 'vbn', 'vbp', 'vbz', 'wdt', 'wp', 'wp$', 'wrb']
		# tags = json.dumps({'cc':0, 'cd':0, 'dt':0, 'ex':0, 'fw':0, 'in':0, 'jj':0, 'jjr':0, 'jjs':0, 'ls':0, 'md':0, 'nn':0, 'nns':0, 'nnp':0, 'nnps':0, 'pdt':0, 'pos':0, 'prp':0,\
		# 	'prp$':0, 'rb':0, 'rbr':0, 'rbs':0, 'rp':0, 'sym':0, 'to':0, 'uh':0, 'vb':0, 'vbd':0, 'vbg':0, 'vbn':0, 'vbp':0, 'vbz':0, 'wdt':0, 'wp':0, 'wp$':0, 'wrb':0})
		# cc = cd = 0

		for ti, tag in enumerate(tag_fd.most_common()):
			print tag
			# try:
			# 	if tags.index(tag[0].lower()):
			# 		print tags[1]
			# except ValueError:
			# 	pass

			if tag[0] == 'CC':
				cc += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'CD':
				cd += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'DT':
				dt += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'EX':
				ex += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'FW':
				fw += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'IN':
				inn += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'JJ':
				jj += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'JJR':
				jjr += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'JJS':
				jjs += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'LS':
				ls += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'MD':
				md += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'NN':
				nn += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'NNS':
				nns += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'NNP':
				nnp += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'NNPS':
				nnps += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'PDT':
				pdt += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'POS':
				pos += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'PRP':
				prps += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'RB':
				rb += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'RBR':
				rbr += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'RBS':
				rbs += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'RP':
				rp += tag[1]
				pos_tags_total += tag[1]		
			elif tag[0] == 'SYM':
				sym += tag[1]
				pos_tags_total += tag[1]	
			elif tag[0] == 'TO':
				to += tag[1]
				pos_tags_total += tag[1]	
			elif tag[0] == 'UH':
				uh += tag[1]
				pos_tags_total += tag[1]	
			elif tag[0] == 'VB':
				vb += tag[1]
				pos_tags_total += tag[1]	
			elif tag[0] == 'VBD':
				vbd += tag[1]
				pos_tags_total += tag[1]	
			elif tag[0] == 'VBG':
				vbg += tag[1]
				pos_tags_total += tag[1]	
			elif tag[0] == 'VBN':
				vbn += tag[1]
				pos_tags_total += tag[1]	
			elif tag[0] == 'VBP':
				vbp += tag[1]
				pos_tags_total += tag[1]	
			elif tag[0] == 'VBZ':
				vbz += tag[1]
				pos_tags_total += tag[1]
			elif tag[0] == 'WDT':
				wdt += tag[1]
				pos_tags_total += tag[1]	
			elif tag[0] == 'WP':
				wp += tag[1]
				pos_tags_total += tag[1]	
			elif tag[0] == 'WPS':
				wps += tag[1]
				pos_tags_total += tag[1]	
			elif tag[0] == 'WRB':
				wrb += tag[1]
				pos_tags_total += tag[1]	
		# if li == 3:
		# 	break
	div = cc / float(pos_tags_total)
	print div		
	print pos_tags_total
	# tags = json.dumps({'cc':{count: cc, percentage, 'cd':cd, 'dt':dt, 'ex':ex, 'fw':fw, 'in':inn, 'jj':jj, 'jjr':jjr, 'jjs':jjs, 'ls':ls, 'md':md, 'nn':nn, 'nns':nns, 'nnp':nnp, 'nnps':nnps, 'pdt':pdt, 'pos':pos, 'prp':prp,\
	# 'prp$':prps, 'rb':rb, 'rbr':rbr, 'rbs':rbs, 'rp':rp, 'sym':sym, 'to':to, 'uh':uh, 'vb':vb, 'vbd':vbd, 'vbg':vbg, 'vbn':vbn, 'vbp':vbp, 'vbz':vbz, 'wdt':wdt, 'wp':wp, 'wp$':wps, 'wrb':wrb, 'pos_tags_total': pos_tags_total})
	with open(report_file, 'w') as outfile:
		outfile.write('CC: ' + str(cc) + '\t Percentage ' + str(cc / float(pos_tags_total) * 100) + '\n')
		outfile.write('CD: ' + str(cd) + '\t Percentage ' + str(cd / float(pos_tags_total) * 100) + '\n')
		outfile.write('DT: ' + str(dt) + '\t Percentage ' + str(dt / float(pos_tags_total) * 100) + '\n')
		outfile.write('EX: ' + str(ex) + '\t Percentage ' + str(ex / float(pos_tags_total) * 100) + '\n')
		outfile.write('FW: ' + str(fw) + '\t Percentage ' + str(fw / float(pos_tags_total) * 100) + '\n')
		outfile.write('IN: ' + str(inn) + '\t Percentage ' + str(inn / float(pos_tags_total) * 100) + '\n')
		outfile.write('JJ: ' + str(jj) + '\t Percentage ' + str(jj / float(pos_tags_total) * 100) + '\n')
		outfile.write('JJR: ' + str(jjr) + '\t Percentage ' + str(jjr / float(pos_tags_total) * 100) + '\n')
		outfile.write('JJS: ' + str(jjs) + '\t Percentage ' + str(jjs / float(pos_tags_total) * 100) + '\n')
		outfile.write('LS: ' + str(ls) + '\t Percentage ' + str(ls / float(pos_tags_total) * 100) + '\n')
		outfile.write('MD: ' + str(md) + '\t Percentage ' + str(md / float(pos_tags_total) * 100) + '\n')
		outfile.write('NN: ' + str(nn) + '\t Percentage ' + str(nn / float(pos_tags_total) * 100) + '\n')
		outfile.write('NNS: ' + str(nns) + '\t Percentage ' + str(nns / float(pos_tags_total) * 100) + '\n')
		outfile.write('NNP: ' + str(nnp) + '\t Percentage ' + str(nnp / float(pos_tags_total) * 100) + '\n')
		outfile.write('NNPS: ' + str(nnps) + '\t Percentage ' + str(nnps / float(pos_tags_total) * 100) + '\n')
		outfile.write('PDT: ' + str(pdt) + '\t Percentage ' + str(pdt / float(pos_tags_total) * 100) + '\n')
		outfile.write('POS: ' + str(pos) + '\t Percentage ' + str(pos / float(pos_tags_total) * 100) + '\n')
		outfile.write('PRP: ' + str(prp) + '\t Percentage ' + str(prp / float(pos_tags_total) * 100) + '\n')
		outfile.write('PRP$: ' + str(prps) + '\t Percentage ' + str(prps / float(pos_tags_total) * 100) + '\n')
		outfile.write('RB: ' + str(rb) + '\t Percentage ' + str(rb / float(pos_tags_total) * 100) + '\n')
		outfile.write('RBR: ' + str(rbr) + '\t Percentage ' + str(rbr / float(pos_tags_total) * 100) + '\n')
		outfile.write('RBS: ' + str(rbs) + '\t Percentage ' + str(rbs / float(pos_tags_total) * 100) + '\n')
		outfile.write('RP: ' + str(rp) + '\t Percentage ' + str(rp / float(pos_tags_total) * 100) + '\n')
		outfile.write('SYM: ' + str(sym) + '\t Percentage ' + str(sym / float(pos_tags_total) * 100) + '\n')
		outfile.write('TO: ' + str(to) + '\t Percentage ' + str(to / float(pos_tags_total) * 100) + '\n')
		outfile.write('UH: ' + str(uh) + '\t Percentage ' + str(uh / float(pos_tags_total) * 100) + '\n')
		outfile.write('VB: ' + str(vb) + '\t Percentage ' + str(vb / float(pos_tags_total) * 100) + '\n')
		outfile.write('VBD: ' + str(vbd) + '\t Percentage ' + str(vbd / float(pos_tags_total) * 100) + '\n')
		outfile.write('VBG: ' + str(vbg) + '\t Percentage ' + str(vbg / float(pos_tags_total) * 100) + '\n')
		outfile.write('VBN: ' + str(vbn) + '\t Percentage ' + str(vbn / float(pos_tags_total) * 100) + '\n')
		outfile.write('VBP: ' + str(vbp) + '\t Percentage ' + str(vbp / float(pos_tags_total) * 100) + '\n')
		outfile.write('VBZ: ' + str(vbz) + '\t Percentage ' + str(vbz / float(pos_tags_total) * 100) + '\n')
		outfile.write('WDT: ' + str(wdt) + '\t Percentage ' + str(wdt / float(pos_tags_total) * 100) + '\n')
		outfile.write('WP: ' + str(wp) + '\t Percentage ' + str(wp / float(pos_tags_total) * 100) + '\n')
		outfile.write('WP$: ' + str(wps) + '\t Percentage ' + str(wps / float(pos_tags_total) * 100) + '\n')
		outfile.write('WRB: ' + str(wrb) + '\t Percentage ' + str(wrb / float(pos_tags_total) * 100) + '\n')


def min_max_tokens(file_list, report_file):
	pos_words_total = 0
	number_of_all_pos_tags_corpus = 0
	minimum_words_per_file = 10000000000000
	min_file = ''
	maximum_words_per_file = 0
	small_list = []
	medium_list = []
	large_list = []
	small_list_count = 0
	medium_list_count = 0
	large_list_count = 0
	text = []
	list_of_pos_no_per_file = []
	tagged_text = []
	for li, line in enumerate(file_list):
		count_pos_words_per_file = 0
		with open(line, 'r') as myfile: 
			whole_text = myfile.read().decode('utf-8')
			myfile.close()
		text_tokenized = word_tokenize(whole_text)
		text_pos_tagged = nltk.pos_tag(text_tokenized)
		tag_fd = nltk.FreqDist(tag for (word, tag) in text_pos_tagged)
		for ind, tag in  enumerate(tag_fd.most_common()):
			count_pos_words_per_file += tag[1]
			number_of_all_pos_tags_corpus += tag[1]
		list_of_pos_no_per_file.append(count_pos_words_per_file)
		if count_pos_words_per_file >= maximum_words_per_file:
			maximum_words_per_file = count_pos_words_per_file
			max_file = line
		if count_pos_words_per_file <= minimum_words_per_file:
			minimum_words_per_file = count_pos_words_per_file
			min_file = line
	print li
	for li, line in enumerate(file_list):
		count_pos_words_per_file = 0
		with open(line, 'r') as myfile: 
			whole_text = myfile.read().decode('utf-8')
			myfile.close()
		text_tokenized = word_tokenize(whole_text)
		text_pos_tagged = nltk.pos_tag(text_tokenized)
		tag_fd = nltk.FreqDist(tag for (word, tag) in text_pos_tagged)
		count_pos_words_per_file = list_of_pos_no_per_file[li]
		print count_pos_words_per_file
		third = (maximum_words_per_file - minimum_words_per_file) / 3
		print minimum_words_per_file	
		if count_pos_words_per_file < minimum_words_per_file + third:
			small_list_count += 1
			small_list.append(line + '\t' + str(count_pos_words_per_file))
		elif count_pos_words_per_file < minimum_words_per_file + 2 * third:
			medium_list_count += 1
			medium_list.append(line + '\t' + str(count_pos_words_per_file))
		else:
			large_list_count += 1
			large_list.append(line + '\t' + str(count_pos_words_per_file))
	with open(report_file, 'w') as outfile:
		outfile.write('Minimum words per file: ' + str(minimum_words_per_file) + '\n')
		outfile.write('Minimum file: ' + min_file + '\n')
		outfile.write('Maximum words per file: ' + str(maximum_words_per_file) + '\n')
		outfile.write('Maximum file: ' + max_file + '\n')
		outfile.write('Small list count: [ ' + str(minimum_words_per_file) + ', ' + str(minimum_words_per_file + third) + ' ]: ' + str(small_list_count) + '\n')
		outfile.write("\n".join(small_list) + '\n')
		outfile.write('Medium list count: [ ' + str(minimum_words_per_file + third) + ', ' + str(minimum_words_per_file + 2 * third) + ' ]: ' + str(medium_list_count) + '\n')
		outfile.write("\n".join(medium_list) + '\n')
		outfile.write('Large list count: [ ' + str(minimum_words_per_file + 2 * third)  + ', ' + str(maximum_words_per_file) + ' ]: ' + str(large_list_count) + '\n')
		outfile.write("\n".join(large_list) + '\n')
		outfile.write('Average pos tags per file: ' + str(number_of_all_pos_tags_corpus/(li + 1)) + '\n')


def get_most_common_verbs(file_list, report_file):
	for li, line in enumerate(file_list):
		count_pos_words_per_file = 0
		with open(line, 'r') as myfile: 
			whole_text = myfile.read().decode('utf-8')
			myfile.close()
		text_tokenized = word_tokenize(whole_text)
		text_pos_tagged = nltk.pos_tag(text_tokenized)
		tag_fd = nltk.FreqDist(text_pos_tagged)
		print [wt[0] for (wt, _) in tag_fd.most_common() if wt[1] == 'VB']
		print line


get_most_common_verbs(get_file_list('sport_train_set.txt'), 'sport_most_common_verbs.txt')
#razdvojiti u 3 kategorije od 0 do 38692

#pos_tag_analysis(get_file_list('sport_train_set_home.txt'), 'report_sport.txt')
#min_max_tokens(get_file_list('sport_train_set.txt'), 'min_max_sport.txt')
