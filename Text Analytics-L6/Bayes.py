import nltk
from nltk.corpus import names
import random

def gender_features_last1(word):
    return {'last_letter': word[-1]}
# gender_features('Shrek') = {'last_letter': 'k'}
def gender_features_last3(word):
    return {'last_3_letters': word[-3:]}

def traning(accuracy_list1, accuracy_list3):
    male_names = [(name, 'male') for name in names.words('male.txt')]
    female_names = [(name, 'female') for name in names.words('female.txt')]
    labeled_names = male_names + female_names
    random.shuffle(labeled_names)
    featuresets_last1 = [(gender_features_last1(n), gender) for (n, gender) in labeled_names]
    random.shuffle(labeled_names)
    featuresets_last3 = [(gender_features_last3(n), gender) for (n, gender) in labeled_names]
    #entries are    ({'last_letter': 'g'}, 'male')
    train_set1, test_set1 = featuresets_last1[500:], featuresets_last1[:500]
    train_set2, test_set2 = featuresets_last3[500:], featuresets_last3[:500]

    classifier_last1 = nltk.NaiveBayesClassifier.train(train_set1)
    classifier_last3 = nltk.NaiveBayesClassifier.train(train_set2)

    # classifier_last1.show_most_informative_features(5)
    accuracy_list1.append(nltk.classify.accuracy(classifier_last1, test_set1))
    # classifier_last3.show_most_informative_features(5)
    accuracy_list3.append(nltk.classify.accuracy(classifier_last3, test_set2))


# ans1 = classifier_last3.classify(gender_features_last3('Mark'))
# ans2 = classifier_last3.classify(gender_features_last3('Precilla'))

# print("Mark is:", ans1)
# print("Precilla is:", ans2)

accuracy_list1 = list()
accuracy_list3 = list()
for i in range(10):
    traning(accuracy_list1, accuracy_list3)

print("average accuracy for last letter: %.3f" % (sum(accuracy_list1)/len(accuracy_list1)))
print("average accuracy for last 3 letters: %.3f" % (sum(accuracy_list3)/len(accuracy_list3)))


