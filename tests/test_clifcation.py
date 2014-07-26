import pygenus
import pytest


def test_totally_male():
    assert pygenus.classify('John') == (1, 0)


def test_totally_female():
    assert pygenus.classify('Trinity') == (0, 1)


def test_totally_fuzzy():
    assert pygenus.classify('Lauren') == (0, 1)


def test_male_pronouns():
    assert pygenus.classify('him') == (1, 0)
    assert pygenus.classify('he') == (1, 0)
    assert pygenus.classify('himself') == (1, 0)
    assert pygenus.classify('his') == (1, 0)


def test_female_pronouns():
    assert pygenus.classify('her') == (0, 1)
    assert pygenus.classify('she') == (0, 1)
    assert pygenus.classify('herself') == (0, 1)
    assert pygenus.classify('hers') == (0, 1)
