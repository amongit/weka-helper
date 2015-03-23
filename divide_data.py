import os, random, shutil

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
				chunks = line.split('\t')
				if chunks:
					self.file_name.append(chunks[0])
					self.url.append(chunks[1])
					self.date.append(chunks[2])
					self.topic = ''.join(chunks[3].split())
				else:
					self.file_name.append(line) 

		self.count = len(self.file_name)
		print len(self.file_name)

	def divide_set_by_percentage(self, count):
		if self.percentage >= 0 and self.percentage <= 100:
			num = int(round(self.percentage / float(100) * self.count))
			train_set_list = random.sample(self.file_name, num)
			train_set = set(train_set_list)
			whole_set = set(self.file_name)
			test_set = whole_set.difference(train_set)
			self.copy_to_folder(train_set, 'train_data')
			self.make_index_file(self.topic + '_train_set.txt', train_set)
			self.copy_to_folder(test_set, 'test_data')
			self.make_index_file(self.topic + '_test_set.txt', test_set)
			return self.check_data_split()
		else:
			raise Exception("Percentage must be between 0 and 100")

	def check_data_split(self):
		if not get_number_of_files(os.getcwd() + '/test_data/' + self.topic) + get_number_of_files(os.getcwd() \
				+ '/train_data/' + self.topic) == get_number_of_files(os.getcwd() + '/' + self.topic):
			return False
		else:
			for f_name in self.file_name:
				if self.check_file_divided(get_name_of_file(f_name)) == False:
					return False
			return True		

	def copy_to_folder(self, list_of_files, folder_dst):
		if os.path.exists(os.getcwd() + '/' + folder_dst + '/' + self.topic): 
			shutil.rmtree(os.getcwd() + '/' + folder_dst + '/' + self.topic)
		if not os.path.exists(os.getcwd() + '/' + folder_dst + '/' + self.topic): 
			os.makedirs(os.getcwd() + '/' + folder_dst + '/' + self.topic)
		for i, l in enumerate(list_of_files):
			shutil.copyfile(l, os.getcwd() + '/' + folder_dst + '/' + self.topic + '/' + get_name_of_file(l))
		return i


	def check_file_divided(self, file_name):
		return os.path.exists(os.getcwd() + '/test_data/' + self.topic + '/' + file_name) \
		 		and not os.path.exists(os.getcwd() + '/train_data/' + self.topic + '/' + file_name) \
		 		or os.path.exists(os.getcwd() + '/train_data/' + self.topic + '/' + file_name) \
		 		or not os.path.exists(os.getcwd() + '/test_data/' + self.topic + '/' + file_name)

	def make_index_file(self, file_name, content):
		with open(file_name, 'w') as f:
			for file_path in content:
				f.write(file_path)
				f.write('\n')


def make_arff_files(folder_src, arff_file_name):
	os.system('java -cp ' + find('weka.jar', '/') + ' weka.core.converters.TextDirectoryLoader -dir ' + folder_src + ' > ' + arff_file_name)

def string_to_vector(arff_train, arff_train_dst, arff_test, arff_test_dst):
	os.system('java -cp ' + find('weka.jar', '/') + ' weka.filters.unsupervised.attribute.StringToWordVector -b -i ' + arff_train + \
			 ' -o ' + arff_train_dst + ' -c last -r ' + arff_test + ' -s ' + arff_test_dst + \
			 ' -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1')
	
	#os.system('java -cp ' + find('weka.jar', '/') + ' weka.filters.unsupervised.attribute.StringToWordVector -b -i train_data.arff -o train_data1.arff -c last -r test_data.arff -s test_data1.arff -R first-last -W 1000 -prune-rate -1.0 -N 0 -stemmer weka.core.stemmers.NullStemmer -M 1')

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
	# os.system('java -cp ' + find('stanford-corenlp-3.5.0.jar', '/') + ':' + find('stanford-corenlp-3.5.0-models.jar', '/') + ':' + find('xom.jar', '/') + \
	# 	':' + find('joda-time.jar', '/') + ':' + find('jollyday.jar', '/') + ':' + find('ejml-0.23.jar', '/') + ' -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP ' + \
	# 	' -annotators tokenize,ssplit,pos,lemma,ner -filelist ' + input_file + ' -outputDirectory ' + output_directory + '')
	os.system('cd ' + find('stanford-corenlp-3.5.0.jar', '/'))
	os.system('java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner -filelist '+ input_file + ' -outputDirectory ' + output_directory + '')
	os.system('cd ' + find('divide_data.py', '/'))
	# os.system('java -cp ' + find('stanford-corenlp-3.5.0.jar', '/') + ' -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,pos,lemma,ner -filelist ' + input_file + ' -outputDirectory ' + output_directory + '')

def open_weka():
	os.system('java -Xmx512m -classpath' + self.find('weka.jar', '/') + ':' + self.find('libsvm.jar', '/') + ' weka.gui.GUIChooser')

#politics_data = Divider(os.getcwd() + '/indexPolitics-work.txt', 60)
#print politics_data.divide_set_by_percentage(politics_data.count)
#politics_data.make_index_file('indexPoliticsNew.txt', politics_data.file_name)

#technology_data = Divider(os.getcwd() + '/indexTechnology-work.txt', 60)
#print technology_data.divide_set_by_percentage(technology_data.count)
#technology_data.make_index_file('indexTechnologyNew.txt', technology_data.file_name)

#sport_data = Divider(os.getcwd() + '/indexSport-work.txt', 60)
#print sport_data.divide_set_by_percentage(sport_data.count)


#make_arff_files('train_data', 'train_data_unparsed.arff')
#make_arff_files('test_data', 'test_data_unparsed.arff')
#string_to_vector('train_data_unparsed.arff', 'train_data_unparsed_string_to_word_vector.arff', 'test_data_unparsed.arff', 'test_data_string_to_word_vector.arff')

stanford_parse('sport_train_set.txt', '/home/dynamic/Desktop/best/git/weka-helper/sport_train_parsed')

#$ java -Xmx512m -classpath //home/dynamic/weka/weka-3-6-11/weka.jar:/home/dynamic/weka/libsvm-3.20/java/libsvm.jar weka.gui.GUIChooser

#open_weka()
#export CLASSPATH="/home/mia/master/weka-3-6-12/weka.jar:/home/mia/master/weka-3-6-12/libsvm-3.20/java/*"
#export CLASSPATH="/home/mia/master/weka-3-6-12/weka.jar:/home/mia/master/weka-3-6-12/libsvm-3.20/java/*"

#java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner -filelist indexPoliticsNew.txt -outputDirectory '/home/dynamic/Desktop/best/git/politics_parsed'

#http://nlp.stanford.edu/software/pos-tagger-faq.shtml