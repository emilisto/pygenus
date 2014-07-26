import sys
from pprint import pprint
import nltk

print "Reading from stdin..."
raw = sys.stdin.read()
tokenized = nltk.word_tokenize(raw)
postags = nltk.pos_tag(tokenized)

pprint(postags)
