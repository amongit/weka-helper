import os, random, shutil, sys

class Divider:
	"""   Class which divides input set into train and test set based on the percentage assigned. """
	
	def __init__(self, index_file, percentage):
		self.file_name = []
		self.url = []
		self.date = []
		self.topic = ''
		self.percentage = percentage

		with open(index_file, 'r') as f:
			for index, line in enumerate(f.readlines()):
				# print index
				# print line
				chunks = line.split('\t')
				if len(chunks) != 4:
					print index
					print line
					break
				if chunks:
					self.file_name.append(chunks[0])
					self.url.append(chunks[1])
					self.date.append(chunks[2])
					self.topic = ''.join(chunks[3].split())
				else:
					print 'ovde'
					#self.file_name.append('madafaka')


		self.count = len(self.file_name)
		print len(self.file_name)

	def divide_set_by_percentage(self, count, train_data_folder, test_data_folder, parent_folder):
		if self.percentage >= 0 and self.percentage <= 100:
			num = int(round(self.percentage / float(100) * self.count))
			train_set_list = random.sample(self.file_name, num)
			train_set = set(train_set_list)
			whole_set = set(self.file_name)
			test_set = whole_set.difference(train_set)
			self.copy_to_folder(train_set, parent_folder + '/' + train_data_folder)
			self.make_index_file(parent_folder + '/' + self.topic + '_' + train_data_folder + '.txt', train_set)
			self.copy_to_folder(test_set,parent_folder +'/' + test_data_folder)
			self.make_index_file(parent_folder + '/' + self.topic + '_' + test_data_folder + '.txt', test_set)
			return self.check_data_split(train_data_folder, test_data_folder, parent_folder)
		else:
			raise Exception("Percentage must be between 0 and 100")

	def check_data_split(self, train_data_folder, test_data_folder, parent_folder):
		if not get_number_of_files(os.getcwd() + '/' + parent_folder + '/' + train_data_folder + '/' + self.topic) + get_number_of_files(os.getcwd() \
				+ '/' + parent_folder + '/' + test_data_folder +'/' + self.topic) == get_number_of_files(os.getcwd() + '/' + self.topic):
			return False
		else:
			for f_name in self.file_name:
				if self.check_file_divided(get_name_of_file(f_name), train_data_folder, test_data_folder) == False:
					return False
			return True		

	def copy_to_folder(self, list_of_files, folder_dst):
		if os.path.exists(os.getcwd() + '/' + folder_dst + '/' + self.topic): 
			shutil.rmtree(os.getcwd() + '/' + folder_dst + '/' + self.topic)
		if not os.path.exists(os.getcwd() + '/' + folder_dst + '/' + self.topic): 
			os.makedirs(os.getcwd() + '/' + folder_dst + '/' + self.topic)
		for i, l in enumerate(list_of_files):
			# print os.path.realpath(l)
			# with open(l, 'r+') as f:
			# 	fgs = f.readlines()
			# 	print fgs
			shutil.copyfile(os.path.realpath(l), os.getcwd() + '/' + folder_dst + '/' + self.topic + '/' + get_name_of_file(l))

	def check_file_divided(self, file_name, train_data_folder, test_data_folder):
		return os.path.exists(os.getcwd() + '/' + test_data_folder + '/' + self.topic + '/' + file_name) \
		 		and not os.path.exists(os.getcwd() + '/' + train_data_folder +'/' + self.topic + '/' + file_name) \
		 		or os.path.exists(os.getcwd() + '/' + train_data_folder +'/' + self.topic + '/' + file_name) \
		 		or not os.path.exists(os.getcwd() + '/' + test_data_folder + '/' + self.topic + '/' + file_name)

	def make_index_file(self, file_name, content):
		with open(file_name, 'w') as f:
			for file_path in content:
				f.write(file_path)
				f.write('\n')


def make_arff_files(folder_src, arff_file_name):
	os.system('java -cp ' + find('weka.jar', '/') + ' weka.core.converters.TextDirectoryLoader -dir ' + folder_src + ' > ' + arff_file_name)

def string_to_vector(arff_train, arff_train_dst, arff_test, arff_test_dst):
	# old filter 
	# os.system('java -cp ' + find('weka.jar', '/') + ' weka.filters.unsupervised.attribute.StringToWordVector -b -i ' + arff_train + \
	# 		 ' -o ' + arff_train_dst + ' -c last -r ' + arff_test + ' -s ' + arff_test_dst + \
	# 		 ' -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1')

	os.system('java -cp ' + find('weka.jar', '/') + ' weka.filters.unsupervised.attribute.StringToWordVector -b -i ' + arff_train + \
			 ' -o ' + arff_train_dst + ' -c last -r ' + arff_test + ' -s ' + arff_test_dst + \
			 ' -R first-last -W 100 -prune-rate -1.0 -T -I -N 2 -S -stemmer weka.core.stemmers.NullStemmer -M 1 -tokenizer weka.core.tokenizers.AlphabeticTokenizer')


	
def get_name_of_file(path):
	return os.path.basename(path)

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def get_number_of_files(path):
	list_dir = []
	list_dir = os.listdir(path)
	count = 0
	for f in list_dir:
		if f.endswith('.txt'):
			count += 1
	return count

def stanford_parse(input_file, output_directory):
	os.system('java -cp ' + find('stanford-corenlp-3.5.0.jar', '/') + ':' + find('stanford-corenlp-3.5.0-models.jar', '/') + ':' + find('xom.jar', '/') + \
		':' + find('joda-time.jar', '/') + ':' + find('jollyday.jar', '/') + ':' + find('ejml-0.23.jar', '/') + ' -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP ' + \
		' -annotators tokenize,ssplit,pos,lemma,ner -filelist ' + input_file + ' -outputDirectory ' + output_directory + '')
	
	# os.system('cd ' + find('stanford-corenlp-3.5.0.jar', '/'))
	# os.system('java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner -filelist '+ input_file + ' -outputDirectory ' + output_directory + '')
	# os.system('cd ' + find('divide_data.py', '/'))
	
	# os.system('java -cp ' + find('stanford-corenlp-3.5.0.jar', '/') + ' -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,pos,lemma,ner -filelist ' + input_file + ' -outputDirectory ' + output_directory + '')

def open_weka():
	#java -Xmx512m -classpath //home/dynamic/weka/weka-3-6-11/weka.jar:/home/dynamic/weka/libsvm-3.20/java/libsvm.jar weka.gui.GUIChooser
	os.system('java -Xmx1280M -classpath ' + find('weka.jar', '/') + ':' + find('libsvm.jar', '/') + ' weka.gui.GUIChooser')

# politics_data = Divider(os.getcwd() + '/indexPolitics-work.txt', 70)
# print politics_data.divide_set_by_percentage(politics_data.count, 'train_70', 'test_70', '70:30')
# #politics_data.make_index_file('indexPoliticsNew.txt', politics_data.file_name)

# technology_data = Divider(os.getcwd() + '/indexTechnology-work.txt', 70)
# print technology_data.divide_set_by_percentage(technology_data.count, 'train_70', 'test_70', '70:30')
 
# sport_data = Divider(os.getcwd() + '/indexSport-work.txt', 70)
# print sport_data.divide_set_by_percentage(sport_data.count, 'train_70', 'test_70' , '70:30')

# make_arff_files('70:30/train_70', '70:30/train_70_unparsed.arff')
# make_arff_files('70:30/test_70', '70:30/test_70_unparsed.arff')

#string_to_vector(find('train_80_unparsed.arff', '/'), '/home/dynamic/Desktop/weka-helper/80:20/train_80_stwv_pruned_to_100.arff', find('test_80_unparsed.arff', '/'), '/home/dynamic/Desktop/weka-helper/80:20/test_80_stwv_pruned_to_100.arff')

open_weka()

# stanford_parse('sport_train_set.txt', '/home/dynamic/Desktop/best/git/weka-helper/sport_train_parsed')


#export CLASSPATH="/home/mia/master/weka-3-6-12/weka.jar:/home/mia/master/weka-3-6-12/libsvm-3.20/java/*"
#export CLASSPATH="/home/mia/master/weka-3-6-12/weka.jar:/home/mia/master/weka-3-6-12/libsvm-3.20/java/*"

#java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner -filelist indexPoliticsNew.txt -outputDirectory '/home/dynamic/Desktop/best/git/politics_parsed'

#http://nlp.stanford.edu/software/pos-tagger-faq.shtml