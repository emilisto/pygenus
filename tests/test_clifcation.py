import pygenus


def test_totally_male():
    assert list(pygenus.classify('John')) == [('John', 'male')]


def test_no_false_positives_for_nouns():
    assert list(pygenus.classify('boy')) == []


def test_totally_female():
    assert list(pygenus.classify('Trinity')) == [('Trinity', 'female')]


def test_totally_fuzzy():
    assert list(pygenus.classify('Lauren')) == [('Lauren', 'female')]


def test_male_pronouns():
    assert list(pygenus.classify('him')) == [('him', 'male')]
    assert list(pygenus.classify('he')) == [('he', 'male')]
    assert list(pygenus.classify('himself')) == [('himself', 'male')]
    assert list(pygenus.classify('his')) == [('his', 'male')]


def test_female_pronouns():
    assert list(pygenus.classify('her')) == [('her', 'female')]
    assert list(pygenus.classify('she')) == [('she', 'female')]
    assert list(pygenus.classify('herself')) == [('herself', 'female')]
    assert list(pygenus.classify('hers')) == [('hers', 'female')]


def test_compound_sentence():
    assert list(pygenus.classify(
        'John is looking for her, but Jane is'
        'nowhere to be found with him.')) == [
            ('John', 'male'),
            ('her', 'female'),
            ('Jane', 'female'),
            ('him', 'male'),
        ]
