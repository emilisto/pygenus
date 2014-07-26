import pygenus
import pytest


def test_totally_male():
    assert pygenus.classify('John') == (1, 0)


def test_totally_female():
    assert pygenus.classify('Trinity') == (0, 1)


def test_totally_fuzzy():
    assert pygenus.classify('Lauren') == (0, 1)


@pytest.xfail('WIP')
def test_male_pronouns():
    assert pygenus.classify('him') == (1, 0)
    assert pygenus.classify('he') == (1, 0)
    assert pygenus.classify('himself') == (1, 0)
    assert pygenus.classify('his') == (1, 0)
