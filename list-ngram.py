#!/usr/bin/python3

import nltk
import pickle
import string
import sys

if len(sys.argv) < 2:
    raise ValueError('Expected pickle filename arg')

f = open(sys.argv[1], 'rb')
finder = pickle.load(f)

ignored_words = nltk.corpus.stopwords.words('spanish')
ignored_words.extend(c for c in string.punctuation)

finder.apply_word_filter(lambda w: w.lower() in ignored_words)

# TODO support generic ngram
bigram_measures = nltk.collocations.BigramAssocMeasures()
for b in finder.nbest(bigram_measures.raw_freq, 10000):
    print(b)

