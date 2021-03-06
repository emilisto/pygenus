import string
import sys
from itertools import chain

import nltk
from nltk.corpus import names


MALE_PRONOUN_SEQ = ('he', 'him', 'his', 'himself')
FEMALE_PRONOUN_SEQ = ('she', 'her', 'hers', 'herself')
NEUTRAL_PRONOUN_SEQ = ('they', 'them', 'their', 'theirs', 'themselves')
ABBREVIATION_SEQ = ('i.e',)
"""Abbreviation last period gets removed by tokenizer."""
PREPOSITION_SEQ = ('for',)

CLASSIFIER_CACHE = None
"""Cache trained classifier."""


class Classifier:

    def __init__(self, classifier=None):
        self.classifier = classifier

    def classify(self, text):
        pos_tag_list = nltk.pos_tag(nltk.word_tokenize(text))

        for pos_tag in pos_tag_list:
            classification = self.classify_word(pos_tag)
            if classification not in ('neutral', 'excess'):
                yield pos_tag[0], classification

    def classify_word(self, pos_tag):
        return self.classifier.classify(_gender_features(pos_tag))


def classify(text):
    _classifier = Classifier(classifier=new_naive_bayes_classifier())
    return _classifier.classify(text)


def new_naive_bayes_classifier():
    # Create feature set consisting of male and female names for training
    global CLASSIFIER_CACHE
    if CLASSIFIER_CACHE:
        return CLASSIFIER_CACHE
    else:
        male_word_seq = _new_training_set(
            'male', names.words('male.txt'), MALE_PRONOUN_SEQ)
        female_word_seq = _new_training_set(
            'female', names.words('female.txt'), FEMALE_PRONOUN_SEQ)
        neutral_pronoun_seq = _new_training_set(
            'neutral', NEUTRAL_PRONOUN_SEQ)
        excess_seq = _new_training_set(
            'excess', ABBREVIATION_SEQ, PREPOSITION_SEQ, string.punctuation,
            ('looking', 'is'),
        )

        featureset_seq = (
            (_gender_features(word), gender)
            for word, gender in chain(
                    male_word_seq,
                    female_word_seq,
                    neutral_pronoun_seq,
                    excess_seq,
            ))
        CLASSIFIER_CACHE = nltk.NaiveBayesClassifier.train(featureset_seq)

        return CLASSIFIER_CACHE


def _new_training_set(tag, *word_seq):
    return (((word, pos_tag), tag)
            for word, pos_tag in
            nltk.pos_tag(list(chain.from_iterable(word_seq))))


def _gender_features(pos_tag):
    word_raw, tag = pos_tag
    word = _normalize_word(word_raw)

    feature_dict = {'pos_tag': tag}

    if word in MALE_PRONOUN_SEQ + FEMALE_PRONOUN_SEQ + NEUTRAL_PRONOUN_SEQ:
        feature_dict = {'pronoun': word}
    elif word in ABBREVIATION_SEQ:
        # XXX: for abbreviations we could check for punctuation and length
        feature_dict = {'abbr': word}
    elif word in PREPOSITION_SEQ:
        feature_dict = {'prep': word}
    elif word in string.punctuation:
        feature_dict = {'punctuation': word}
    elif any(map(tag.startswith, ['VB', 'TO', 'DT', 'IN'])):
        feature_dict.update({'some_oher_stuff': word})
    else:
        feature_dict.update({'last_letters': word[-2:]})

    return feature_dict


def _normalize_word(word_raw):
    return word_raw.lower()


def main():
    """Take input from stdin and print all matches as word, tag tuples."""
    try:
        for match in classify(sys.stdin.read()):
            print(match)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
