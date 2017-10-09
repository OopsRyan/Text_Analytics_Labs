import nltk
import os
import math
from nltk.corpus import stopwords


def print_vector_space_model(term_dict, vect_title):
	print('\n------------------------------------------')
	print ("\n\t%s Matrix\n" % (vect_title))
	print ("\tDocutment1")
	for k,v in term_dict.items():
		print("\t"+str(v)+"\t"+k)

### join Text from tf_idf_scores
def print_keys_in_dict(iterms_dict):
	iterms_text = ' '.join( k for k,v in iterms_dict.items())
	print("\n%s\n" % iterms_text) 

## TF ------- count / length 
def calculate_tf_score(tf_dict, length_of_corpus):
	tf_scores = dict()
	## normalized by dividing by the total number of words in corpus
	for k,v in tf_dict.items():
		tf_scores[k] = v / len(corpus)
	return tf_scores

## IDF ------- log(length / (1 + count)) ------- For frequency > 1
def calculate_idf_score(tf_dict, length_of_corpus):
	idf_scores = dict()
	for k,v in tf_dict.items():
		if v > 1:
			idf_scores[k] = math.log(len(corpus) / (1 + v))
	return idf_scores

### TF-IDF --------- tf * idf ------- For frequency > 1
def calculate_tf_idf_scores(tf_scores, idf_scores, length_of_corpus):
	tf_idf_scores = dict()
	tf_idf_scores = {k1 : v1*v2 for k1,v1 in tf_scores.items() for k2,v2 in idf_scores.items() if k1 == k2}
	return tf_idf_scores


stop = stopwords.words('english')

rawtext = open(os.getcwd() + os.sep + 'items.txt').read()
 
## removal of stopwords
corpus = [word for word in rawtext.split() if word not in stop]
print(corpus)

text = ' '.join(corpus)
print(text)

tf_dict = dict()
for word in corpus:
	tf_dict[word] = tf_dict.get(word, 0) + 1

## sorting
tf_dict = {k: tf_dict[k] for k in sorted(tf_dict, key=tf_dict.get, reverse = True)}

## calculate tf scores
tf_scores = dict()
tf_scores = calculate_tf_score(tf_dict, len(corpus))
print_vector_space_model(tf_scores, "TF Scores")


## calculate idf scores
idf_scores = dict()
idf_scores = calculate_idf_score(tf_dict, len(corpus))
print_vector_space_model(idf_scores, "IDF Scores")

# print('\n------------------------------------------\n')

## calculate tf-idf scores
tf_idf_scores = dict()
tf_idf_scores = calculate_tf_idf_scores(tf_scores, idf_scores, len(corpus))
print_vector_space_model(tf_idf_scores, "TF-IDF Scores")

## print all keys in tf_idf iterms, frequencies of which are more than 1
print_keys_in_dict(tf_idf_scores)











