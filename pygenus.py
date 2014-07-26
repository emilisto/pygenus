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


def classify_word(word):
    classifier = new_classifier()
    return classifier.classify(gender_features(word))

def classify(text):
    counter = Counter(classify_word(word) for word in text.split())
    return counter['male'], counter['female']
