#!/usr/bin/python3

import nltk
import pickle
import sys
from nltk.collocations import *

n = 2

if len(sys.argv) > 1:
    if argv[1].is_digit():
        n = int(argv[1])
        del argv[1]
    if len(sys.argv) > 1 and argv[1] != 'cess_esp':
        raise ValueError('Unknown corpus {}'.format(argv[1]))
    tokens = nltk.corpus.cess_esp.words()
else:
    tokens = nltk.tokenize.word_tokenize(sys.stdin.read(), language='spanish')

t = { 2: BigramCollocationFinder, 3: TrigramCollocationFinder, 4: QuadgramCollocationFinder}

finder = t[n].from_words(tokens)
finder.apply_freq_filter(3)

pickle.dump(finder, sys.stdout.buffer)

