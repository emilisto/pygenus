from collections import Counter

import nltk
from nltk.corpus import names


def gender_features(word):
    return {'last_letters': word[-2:]}


def new_classifier():
    labeled_names = ([(name, 'male') for name in names.words('male.txt')]
                     + [(name, 'female') for name in names.words('female.txt')])
    featuresets = [(gender_features(n), gender)
                   for (n, gender) in labeled_names]
    return nltk.NaiveBayesClassifier.train(featuresets)


def classify(text):
    classifier = new_classifier()
    counter = Counter([classifier.classify(gender_features(text))])
    return counter['male'], counter['female']
