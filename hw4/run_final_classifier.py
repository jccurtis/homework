def run_final_classifier(path,forest='classifier.npy'):
	'''
	Run Final Classifier uses the random forest classifier called 
	trained_classifier I built with the full 4244 image training set. 
	It must be in the same directory as this run_final_classifier.py 
	function. 
	'''

	from os import listdir
	from functions import split_seq, extract_features

	print 'filename          predicted_class'
	print '------------------------------------------'

	for im_name in listdir(path):


	return None