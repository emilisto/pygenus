import pygenus
import pytest


def classify(text):
    return list(pygenus.classify(text))


def test_totally_male():
    assert classify('John') == [('John', 'male')]


def test_no_false_positives_for_nouns():
    assert classify('boy') == []


def test_totally_female():
    assert classify('Trinity') == [('Trinity', 'female')]


def test_totally_fuzzy():
    assert classify('Lauren') == [('Lauren', 'female')]


@pytest.mark.parametrize('pronoun', pygenus.MALE_PRONOUN_SEQ)
def test_classify_male_pronouns_as_male(pronoun):
    assert classify(pronoun) == [(pronoun, 'male')]


@pytest.mark.parametrize('pronoun', pygenus.FEMALE_PRONOUN_SEQ)
def test_classify_female_pronouns_as_female(pronoun):
    assert classify(pronoun) == [(pronoun, 'female')]


@pytest.mark.parametrize('pronoun', pygenus.NEUTRAL_PRONOUN_SEQ)
def test_filter_out_gender_neutral_pronouns(pronoun):
    assert classify(pronoun) == []


def test_compound_sentence():
    text = ('John is looking for her, but Jane is'
            'nowhere to be found with him.')

    classifications = sorted(classify(text))

    assert classifications == sorted([
        ('John', 'male'),
        ('her', 'female'),
        ('Jane', 'female'),
        ('him', 'male'),
    ])


def test_dont_include_abbreviations():
    assert_ignores_word(
        'All the mark of Adam: all who bear the mark of Adam i.e. all men',
        'i.e')


def test_dont_include_punctuation():
    assert_ignores_word(
        'No wonder is though Jove her stellify, <33> As '
        'telleth Agathon, <34> for her goodness;',
        '<')


def test_dont_include_numbers():
    assert_ignores_word(
        'Notes to The prologue to The Legend of Good Women 1. Bernard.',
        '1.')


def test_defines_all_neutral_pronouns():
    assert sorted(pygenus.NEUTRAL_PRONOUN_SEQ) == \
        sorted(('they', 'them', 'their', 'theirs', 'themselves'))


def test_defines_all_male_pronouns():
    assert sorted(pygenus.MALE_PRONOUN_SEQ) == \
        sorted(('him', 'he', 'his', 'himself'))


def test_defines_all_female_pronouns():
    assert sorted(pygenus.FEMALE_PRONOUN_SEQ) == \
        sorted(('she', 'her', 'hers', 'herself'))


def test_has_training_set_for_abbrevations():
    assert sorted(pygenus.ABBREVIATION_SEQ) == \
        sorted(('i.e',))


def test_has_training_set_for_prepositions():
    assert sorted(pygenus.PREPOSITION_SEQ) == \
        sorted(('for',))


def assert_ignores_word(text, unexpected_word):
    classifications = classify(text)
    assert unexpected_word not in [word for word, _ in classifications]
