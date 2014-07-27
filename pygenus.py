import sys
from itertools import chain

import nltk
from nltk.corpus import names


MALE_PRONOUN_SEQ = ('he', 'him', 'his', 'himself')
FEMALE_PRONOUN_SEQ = ('she', 'her', 'hers', 'herself')
NEUTRAL_PRONOUN_SEQ = ('they', 'them', 'their', 'theirs', 'themselves')


class Classifier:

    def __init__(self, classifier=None):
        self.classifier = classifier

    def classify(self, text):
        # Here goes all data preprocessing
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
            tag = self.classify_word(word)
            if tag != 'neutral':
                yield word, self.classify_word(word)

    def classify_word(self, word):
        if word in MALE_PRONOUN_SEQ:
            return 'male'
        elif word in FEMALE_PRONOUN_SEQ:
            return 'female'
        elif word in NEUTRAL_PRONOUN_SEQ:
            return 'neutral'
        # Default to classifier and and real analysis
        else:
            return self.classifier.classify(_gender_features(word))


def _gender_features(word):
    return {'last_letters': word[-2:]}


def classify(text):
    _classifier = Classifier(classifier=new_naive_bayes_classifier())
    return _classifier.classify(text)


def new_naive_bayes_classifier():
    # Create featureset consiting of male and female names for training
    male_name_seq = ((name, 'male') for name in names.words('male.txt'))
    female_name_seq = ((name, 'female') for name in names.words('female.txt'))

    featureset_seq = (
        (_gender_features(word), gender)
        for word, gender in chain(male_name_seq, female_name_seq))

    # Train and return ready classifier
    return nltk.NaiveBayesClassifier.train(featureset_seq)


def main():
    """Take input from stdin and print all matches as word, tag tuples."""
    for match in classify(sys.stdin.read()):
        print(match)


if __name__ == '__main__':
    main()
