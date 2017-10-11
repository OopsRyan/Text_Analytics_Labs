import math
import nltk
import os


def entropy(labels):
	freqdist = nltk.FreqDist(labels)
	probs = [freqdist.freq(l) for l in freqdist]
	return -sum(p * math.log(p,2) for p in probs)

spam_file = "spam_set.txt"
random_file = "random_set.txt"
spam_rawtext = open((os.getcwd() + os.sep + spam_file), encoding="utf-8").read()
random_rawtext = open((os.getcwd() + os.sep + random_file), encoding="utf-8").read()

spam_tweets = spam_rawtext.split()
random_tweets = random_rawtext.split()

print ("spam entropy : %.5f" % (entropy(spam_tweets) ))#/ len(spam_tweets)))

print ("random entropy : %.5f" % (entropy(random_tweets)))# / len(random_tweets)))

all_tweets = spam_tweets + random_tweets
print ("all entropy : %.5f" % (entropy(all_tweets) ))#/ len(all_tweets)))