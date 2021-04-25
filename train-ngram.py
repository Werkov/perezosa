#!/usr/bin/python3

import nltk
import pickle
import sys
from nltk.collocations import *

n = 2

if len(sys.argv) > 1:
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
        del sys.argv[1]

if len(sys.argv) < 2:
    raise ValueError('Expected pickle filename arg')

f = open(sys.argv[1], 'rb')
tokens = pickle.load(f)

t = { 2: BigramCollocationFinder, 3: TrigramCollocationFinder, 4: QuadgramCollocationFinder}

finder = t[n].from_words(tokens)
finder.apply_freq_filter(3)

pickle.dump(finder, sys.stdout.buffer)

