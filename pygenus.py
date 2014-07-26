from collections import Counter

import nltk
from nltk.corpus import names

MALE_PRONOUN_SEQ = ('he', 'him', 'his', 'himself')
FEMALE_PRONOUN_SEQ = ('she', 'her', 'hers', 'herself')


def gender_features(word):
    return {'last_letters': word[-2:]}


def new_classifier():
    labeled_names = ([(name, 'male') for name in names.words('male.txt')]
                     + [(name, 'female') for name in names.words('female.txt')])
    featuresets = [(gender_features(n), gender)
                   for (n, gender) in labeled_names]
    return nltk.NaiveBayesClassifier.train(featuresets)


def classify_word(word):
    if word in MALE_PRONOUN_SEQ:
        return 'male'
    elif word in FEMALE_PRONOUN_SEQ:
        return 'female'
    else:
        classifier = new_classifier()
        return classifier.classify(gender_features(word))


def classify(text):
    counter = Counter(classify_word(word) for word in text.split())
    return counter['male'], counter['female']
