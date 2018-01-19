# coding:utf-8
import os
import math
from nltk.corpus import stopwords
import numpy as np


### print the matrix by taking a dict
def print_dict_to_matrix(term_dict, vect_title):
    print('\n------------------------------------------')
    print("\n\t%s\n" % (vect_title))
    print("\tDocutment1")
    for k, v in term_dict.items():
        print("\t%s\t%0.2f\t" % (format(k, '<30'), v))


def print_array_to_matrix(tf_array, term_dict, vect_title):
    print('\n------------------------------------------')
    print("\n\t%s\n" % (vect_title))
    i = 0
    for k, v in term_dict.items():
        print("\t%s\t%s" % (tf_array[i], k))
        i += 1


### join Text from tf_idf_scores
def get_keys_in_dict(terms_dict):
    terms_text = ' '.join(k for k, v in terms_dict.items())
    return terms_text


### sort dict in descending order
def sort_dict_des(target_dict):
    return {k: target_dict[k] for k in sorted(target_dict, key=target_dict.get, reverse=True)}


# ## TF ------- count / length
# def calculate_tf_weights(tf_dict, length_of_corpus):
#     tf_scores = dict()
#     ## normalized by dividing by the total number of words in corpus
#     for k, v in tf_dict.items():
#         tf_scores[k] = v / len(corpus)
#     return tf_scores


## IDF ------- log(length / (1 + count)) ------- For frequency > 1
def calculate_idf(tf_dict, items_number):
    idf_dict = dict()
    for k, v in tf_dict.items():
        if v > 1:
            idf_dict[k] = float('%0.1f' % math.log10(items_number / v))
    return idf_dict


### TF-IDF --------- tf * idf ------- For frequency > 1
def calculate_tf_idf_scores(tf_array, idf_dict):
    tf_idf_scores = list()
    i = 0
    # print(tf_idf_scores)
    for k, v in idf_dict.items():
        tf_idf_scores += [i for i in (v * tf_array[i])]
        i += 1
    return np.array(tf_idf_scores)

### PMI(x,y) = log(c(x,y)) + log(N) - log(c(x)) - log(c(y))
### x = corpus[i]
### y = corpus[i+1]
### N = len(corpus)
### x + y = corpus[i] + corpus(i+1) = pointwise
def calculate_pmi_scores(corpus, adjacent_pairs):
    corpus_text = ' '.join(corpus)
    pmi_array = []
    i = 0
    for pointwise,count in adjacent_pairs.items():
        x = corpus[i]
        y = corpus[i+1]
        n = len(corpus)
        pointwise = x + " " + y
        cx = corpus_text.count(x)
        cy = corpus_text.count(y)
        cxy = corpus_text.count(pointwise)
        pmi = math.log(cxy) + math.log(n) - math.log(cx) - math.log(cy)
        pmi_array += [x, y, cxy, cx, cy, float('%.2f' % pmi)]
        i += 1
    return pmi_array

def get_adjacent_pairs(corpus):
    corpus_text = ' '.join(corpus)
    adjacent_pairs = dict()

    for i in range(len(corpus) - 1):
        pointwise = corpus[i] + ' ' + corpus[i + 1]
        adjacent_pairs[pointwise] = adjacent_pairs.get(pointwise, 0) + corpus_text.count(pointwise)

    return sort_dict_des(adjacent_pairs)



file_name = 'items.txt'
# file_name = 'items_without_punctuation.txt'

stop = stopwords.words('english')
rawtext = open(os.getcwd() + os.sep + file_name, encoding='utf-8').read()
# rawtext = nltk.word_tokenize(rawtext)
# print(rawtext)
print("\n\n")

items_list = rawtext.split('\n')

## removal of stopwords
corpus = [word for word in rawtext.split() if word not in stop]
print(corpus)

text = ' '.join(corpus)
print(text)

# get all keys in corpus
df_dict = dict()
for word in corpus:
    df_dict[word] = 0

# calculate df 
for k,v in df_dict.items():
	for item in items_list:
		if k in item:
			df_dict[k] += 1

## sorting------extremely important!!!!  if do not sort, the order will be broken.
df_dict = sort_dict_des(df_dict)

## count keys in each item_text
tf_array = np.array([item.count(k) for k, v in df_dict.items() for item in items_list])
tf_array = tf_array.reshape(len(df_dict), len(items_list))
## print tf martix
print_array_to_matrix(tf_array, df_dict, "TF Matrix")

# ## calculate tf weights
# tf_weights = dict()
# tf_weights = calculate_tf_weights(df_dict, len(corpus))
# # print_dict_to_matrix(tf_weights, "TF Scores Matrix")

# print DF
print_dict_to_matrix(df_dict, "DF Matrix")

## calculate idf scores
idf_dict = calculate_idf(df_dict, len(items_list))
print_dict_to_matrix(idf_dict, "IDF Matrix")

## calculate tf-idf scores
tf_idf_scores = calculate_tf_idf_scores(tf_array, idf_dict).reshape(len(idf_dict), len(items_list))
print_array_to_matrix(tf_idf_scores, idf_dict, "TF-IDF Scores Matrix")

## print all keys in tf_idf dict, frequencies of which are more than 1
print("--------- the frequency of a term in items more than 1 ---------")
print(get_keys_in_dict(idf_dict))
frequency_more_than_1_text = ' '.join([ term for term in corpus if df_dict[term] > 1])
print(frequency_more_than_1_text)


############# PMI #############
### get top 10 frequent adjacent pairs
adjacent_pairs = get_adjacent_pairs(corpus)
print_dict_to_matrix(adjacent_pairs, "Adjacent pairs count")
### caluculate pmi socres
pmi_array = calculate_pmi_scores(corpus, adjacent_pairs)
# print(pmi_array)
# pmi_array = np.array(pmi_array)
# pmi_array = pmi_array.reshape(len(adjacent_pairs), 6)
# print_array_to_matrix(pmi_array, "PMI Scores Matrix")
print('\n------------------------------------------')
print("\n\t%s\n" % ("PMI Score Matrix"))
i = 0
print("\t%s\t%s\t%s\t%s\t%s\t%s" % (format('x', '^20'), format('y', '^20'), format('c(x,y)', '^5'), format('c(x)', '^5'), format('c(y)', '^5'), format('pmi', '^5')))
for k,v in adjacent_pairs.items():
    print("\t%s\t%s\t%s\t%s\t%s\t%s" % (format(pmi_array[i*6], '^20'), format(pmi_array[i*6+1], '^20'), format(pmi_array[i*6+2], '^5'), format(pmi_array[i*6+3], '^5'), format(pmi_array[i*6+4], '^5'), format(pmi_array[i*6+5], '^5')))
    i += 1


# print(pmi_scores["data preprocessing"])
