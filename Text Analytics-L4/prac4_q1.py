import nltk
import os
import math


from nltk.corpus import stopwords
stop = stopwords.words('english')

rawtext = open(os.getcwd() + os.sep + 'items.txt').read()
 
text_without_stopwords = [word for word in rawtext.split() if word not in stop]
print(text_without_stopwords)

text = ' '.join(text_without_stopwords)
print(text)

tf_dict = dict()
for word in text_without_stopwords:
	tf_dict[word] = tf_dict.get(word, 0) + 1

## sorting
tf_dict = {k: tf_dict[k] for k in sorted(tf_dict, key=tf_dict.get, reverse = True)}

## DF ------- count / length 
tf_scores = dict()
## normalized by dividing by the total number of words in text_without_stopwords
for k,v in tf_dict.items():
	tf_scores[k] = v / len(text_without_stopwords)

for k,v in tf_scores.items():
	print(k+' : '+ str(v))

print('\n------------------------------------------\n')

## IDF ------- log(length / (1 + count)) ------- For frequency > 1
idf_scores = dict()
for k,v in tf_dict.items():
	if v > 1:
		idf_scores[k] = math.log(len(text_without_stopwords) / (1 + v))

for k,v in idf_scores.items():
	print(k+' : '+str(v))

print('\n------------------------------------------\n')

### TF-IDF --------- tf * idf ------- For frequency > 1
tf_idf_scores = dict()
tf_idf_scores = {k1 : v1*v2 for k1,v1 in tf_scores.items() for k2,v2 in idf_scores.items() if k1 == k2}
for k,v in tf_idf_scores.items():
	print(k+' : '+str(v))

### join Text from tf_idf_scores
tf_idf_text = ' '.join( k for k,v in tf_idf_scores.items())
print(tf_idf_text) 