#!/usr/bin/python3

import nltk
import pickle
import string
import sys
from nltk.collocations import *

if len(sys.argv) < 2:
    raise ValueError('Expected pickle filename arg')

f = open(sys.argv[1], 'rb')
finder = pickle.load(f)

f_map = {
        BigramCollocationFinder: 2,
        TrigramCollocationFinder: 3,
        QuadgramCollocationFinder: 4,
        }
measure_map = {
        2: nltk.collocations.BigramAssocMeasures,
        3: nltk.collocations.TrigramAssocMeasures,
        4: nltk.collocations.QuadgramAssocMeasures,
        }
n = f_map[type(finder)]

manual_stopwords = {
        2: nltk.corpus.stopwords.words('spanish'),
        3: ['el', 'la', 'los', 'las'],
        4: [],
        }
ignored_words = manual_stopwords[n]
ignored_words.extend(c for c in string.punctuation)
# Wiki specific tokens
ignored_words.extend(['==', '``', "''", '»', '«', '“'])

ignored_words = set(ignored_words)

finder.apply_word_filter(lambda w: w.lower() in ignored_words)

ngram_measures = measure_map[n]()
for b in finder.nbest(ngram_measures.raw_freq, 10000):
    print(b)

