import pygenus
import pytest


def test_totally_male():
    assert list(pygenus.classify('John')) == [('John', 'male')]


def test_no_false_positives_for_nouns():
    assert list(pygenus.classify('boy')) == []


def test_totally_female():
    assert list(pygenus.classify('Trinity')) == [('Trinity', 'female')]


def test_totally_fuzzy():
    assert list(pygenus.classify('Lauren')) == [('Lauren', 'female')]


@pytest.mark.parametrize('pronoun', pygenus.MALE_PRONOUN_SEQ)
def test_classify_male_pronouns_as_male(pronoun):
    assert list(pygenus.classify(pronoun)) == [(pronoun, 'male')]


@pytest.mark.parametrize('pronoun', pygenus.FEMALE_PRONOUN_SEQ)
def test_classify_female_pronouns_as_female(pronoun):
    assert list(pygenus.classify(pronoun)) == [(pronoun, 'female')]


@pytest.mark.parametrize('pronoun', pygenus.NEUTRAL_PRONOUN_SEQ)
def test_filter_out_gender_neutral_pronouns(pronoun):
    assert list(pygenus.classify(pronoun)) == []


def test_compound_sentence():
    assert list(pygenus.classify(
        'John is looking for her, but Jane is'
        'nowhere to be found with him.')) == [
            ('John', 'male'),
            ('her', 'female'),
            ('Jane', 'female'),
            ('him', 'male'),
        ]


def test_defines_all_neutral_pronouns():
    assert sorted(pygenus.NEUTRAL_PRONOUN_SEQ) == \
        sorted(('they', 'them', 'their', 'theirs', 'themselves'))


def test_defines_all_male_pronouns():
    assert sorted(pygenus.MALE_PRONOUN_SEQ) == \
        sorted(('him', 'he', 'his', 'himself'))


def test_defines_all_female_pronouns():
    assert sorted(pygenus.FEMALE_PRONOUN_SEQ) == \
        sorted(('she', 'her', 'hers', 'herself'))
