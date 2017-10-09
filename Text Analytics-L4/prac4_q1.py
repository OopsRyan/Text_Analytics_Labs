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
        print("\t%0.4f\t\t%s" % (v, k))


def print_array_to_matrix(term_array, term_dict, vect_title):
    print('\n------------------------------------------')
    print("\n\t%s\n" % (vect_title))
    i = 0
    for k, v in term_dict.items():
        print("\t%s\t%s" % (term_array[i], k))
        i += 1


### join Text from tf_idf_scores
def get_keys_in_dict(terms_dict):
    terms_text = ' '.join(k for k, v in terms_dict.items())
    return terms_text


### descending sort dict 
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
    idf_scores = dict()
    for k, v in tf_dict.items():
        if v > 1:
            idf_scores[k] = math.log10(items_number / v)
    return idf_scores


### TF-IDF --------- tf * idf ------- For frequency > 1
def calculate_tf_idf_scores(tf_scores, idf_scores, length_of_corpus):
    tf_idf_scores = dict()
    tf_idf_scores = {k1: v1 * v2 for k1, v1 in tf_scores.items() for k2, v2 in idf_scores.items() if k1 == k2}
    return tf_idf_scores


### PMI(x,y) = log(c(x,y)) + log(N) - log(c(x)) - log(c(y))
### x = corpus[i]
### y = corpus[i+1]
### N = len(corpus)
### x + y = corpus[i] + corpus(i+1) = pointwise
def calculate_pmi_scores(corpus):
    corpus_text = ' '.join(corpus)
    pmi_scores = dict()
    for i in range(len(corpus) - 1):
        pointwise = corpus[i] + ' ' + corpus[i + 1]
        pmi_scores[pointwise] = math.log(corpus_text.count(pointwise)) + math.log(len(corpus)) \
                                - math.log(corpus_text.count(corpus[i])) - math.log(corpus_text.count(corpus[i + 1]))
    return pmi_scores


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

# df in corpus
df_dict = dict()
for word in corpus:
    df_dict[word] = df_dict.get(word, 0) + 1

## sorting------extremely important!!!!  if do not sort, the order will be broken.
df_dict = sort_dict_des(df_dict)

## count keys in each item_text
terms_array = np.array([item.count(k) for k, v in df_dict.items() for item in items_list])
terms_array = terms_array.reshape(len(df_dict), len(items_list))
## print tf martix
print_array_to_matrix(terms_array, df_dict, "TF Matrix")

# ## calculate tf weights
# tf_weights = dict()
# tf_weights = calculate_tf_weights(df_dict, len(corpus))
# # print_dict_to_matrix(tf_weights, "TF Scores Matrix")

# print DF
# print_dict_to_matrix(df_dict, "DF Matrix")

## calculate idf scores
idf_dict = dict()
idf_dict = calculate_idf(df_dict, len(terms_array))
print_dict_to_matrix(idf_dict, "IDF Matrix")

## calculate tf-idf scores
tf_idf_scores = dict()
tf_idf_scores = calculate_tf_idf_scores(df_dict, idf_dict, len(corpus))
# print_dict_to_matrix(tf_idf_scores, "TF-IDF Scores Matrix")

## print all keys in tf_idf dict, frequencies of which are more than 1
print("--------- the frequency of iterms more than 1 ---------")
# print(get_keys_in_dict(tf_idf_scores))

### caluculate pmi socres
pmi_scores = sort_dict_des(calculate_pmi_scores(corpus))
# print_dict_to_matrix(pmi_scores, "PMI Scores Matrix")
