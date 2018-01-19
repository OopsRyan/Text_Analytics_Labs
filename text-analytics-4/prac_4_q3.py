import math, string, sys, fileinput, os

def range_bytes (): return range(256)
def range_printable(): return (ord(c) for c in string.printable)
def H(data, iterator=range_bytes):
    if not data:
        return 0
    entropy = 0
    for x in iterator():
        p_x = float(data.count(chr(x)))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy
    

spam_file = "spam_set.txt"
random_file = "random_set.txt"
spam_rawtext = open((os.getcwd() + os.sep + spam_file), encoding="utf-8").read()
random_rawtext = open((os.getcwd() + os.sep + random_file), encoding="utf-8").read()

spam_tweets = spam_rawtext.split('\n')
random_tweets = random_rawtext.split('\n')

i = 0
for str in spam_tweets:
    print ("spam tweet %d : %f" % (i, H(str, range_printable)))
    i += 1

spam_str = ' '.join(spam_tweets)
print ("spam_tweets: %f" % H(spam_str, range_printable))

i = 0
for str in random_tweets:
    print ("random tweet %d : %f" % (i, H(str, range_printable)))
    i += 1

random_str = ' '.join(random_tweets)
print ("random_tweets: %f" % H(random_str, range_printable))

all_str = spam_str + random_str
print ("all_tweets: %f" % H(all_str, range_printable))


