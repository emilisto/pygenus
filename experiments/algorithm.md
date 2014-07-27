# Algorithm Outline

In each step, all identified gender words should be removed from the
working set, so it's not additionally analyzed by the next step.

1. Produce working set: tokenize and tag all words using NLTK
2. Gender words: Extract all _pronouns_ and classify them, remove
   identified words from the working set - i.e. `he`, `she`, etc.
3. Names: Extract all _proper nouns_ and:
  a. Identify names by using a list
  b. Identify names using Bayesian classifier

Extending to other languages than English. We can prolly not use NLTK
anymore then.

# Testing

The basic classification should be tested on a vocabulary of words that
have been manually classified as one of: male, female or neutral. The
tests shall fall in two categories:

- Absolute tests: only pass the test iff every word must be correctly
  classified in order for the
- Threshold test: pass the test iff more than a threshold fraction of
  the words are correctly classified.
