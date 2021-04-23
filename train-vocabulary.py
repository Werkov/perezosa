#!/usr/bin/python3

import nltk
import pickle
import sys
from collections import Counter

if len(sys.argv) > 1:
    if argv[1] != 'cess_esp':
        raise ValueError('Unknown corpus {}'.format(argv[1]))
    tokens = nltk.corpus.cess_esp.words()
else:
    tokens = nltk.tokenize.word_tokenize(sys.stdin.read(), language='spanish')

counter = Counter(tokens)

pickle.dump(counter, sys.stdout.buffer)
