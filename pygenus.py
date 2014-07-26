from collections import Counter
import sys

import nltk
from nltk.corpus import names

MALE_PRONOUN_SEQ = ('he', 'him', 'his', 'himself')
FEMALE_PRONOUN_SEQ = ('she', 'her', 'hers', 'herself')


class Classifier:

    def __init__(self):
        self.names = (
            [(name, 'male') for name in names.words('male.txt')] +
            [(name, 'female') for name in names.words('female.txt')]
        )

        featuresets = [(self._gender_features(n), gender)
                       for (n, gender) in self.names]
        self.bayes_classifier = nltk.NaiveBayesClassifier.train(featuresets)

    def classify_word(self, word):
        if word in MALE_PRONOUN_SEQ:
            return 'male'
        elif word in FEMALE_PRONOUN_SEQ:
            return 'female'
        # Default to Bayes classifier
        else:
            return self.bayes_classifier.classify(self._gender_features(word))

    def classify(self, text):
        tokenized = nltk.word_tokenize(text)
        tagged_words = nltk.pos_tag(tokenized)

        def is_possible_gender_word(wordtag):
            word, tag = wordtag
            # TODO: narrow down the word classes as much as possible - possibly
            # include NNP and NNS instead of NN
            desired_tags = ('PRP', 'NNS', 'NNP')
            return any(tag.startswith(desired_tag) for desired_tag in desired_tags)

        words = [
            word for word, tag in
            filter(is_possible_gender_word, tagged_words)
        ]

        for word in words:
            yield word, self.classify_word(word)

    def _gender_features(self, word):
        return {'last_letters': word[-2:]}


_classifier = None


def classify(text):
    global _classifier
    if _classifier is None:
        _classifier = Classifier()
    return _classifier.classify(text)



if __name__ == '__main__':
    for match in classify(sys.stdin.read()):
        print(match)
