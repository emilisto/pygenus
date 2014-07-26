# Overview

## Requirements

Given a URL, identify return the "gender words" found on the page. Each
gender word should be classified as either female or male.

- Need a marker for the page and location of each gender word

## Classifier

Reads a stream of text and return the identified gender words.

## Crawler service

Given a URL, it shall perform a crawl to a specified depth and return
the total raw text found, with "nonsense characters" stripped.

# Gender analyzer

The analyzer shall accept natural language text and emit identified
_gender words_.

The analyzer shall split the text into words and feed each word into a
classifier which says whether the word is either neutral, female or
male.

If the word is a gender word, the following should be provided:

- Whether it is male or female
- Whether the word is a name, pronoun, etc.
- The location of the word in the text

The classifier accepts natural language text and emits identified gender
words, along with their position in the provided text.

## Using nltk

Interesting tags:

- NNP: noun, proper, singular
- PRP: pronoun, personal

Identify things like:

    ("''", "''"),
    ('Miss', 'NNP'),
    ('Manette', 'NNP'),
    ('had', 'VBD'),

    ...

    ('to', 'TO'),
    ('Mr.', 'NNP'),
    ('Jarvis', 'NNP'),
    ('Lorry.', 'NNP'),
    ("''", "''"),

By trying to group consecutive NNP's.


# Sources

 - https://docs.djangoproject.com/en/dev/internals/contributing/writing-documentation/
