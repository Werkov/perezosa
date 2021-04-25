#!/usr/bin/python3

import nltk
import pickle
import sys


if len(sys.argv) > 1:
    if argv[1] != 'cess_esp':
        raise ValueError('Unknown corpus {}'.format(argv[1]))
    tokens = nltk.corpus.cess_esp.words()
else:
    tokens = nltk.tokenize.word_tokenize(sys.stdin.read(), language='spanish')

pickle.dump(tokens, sys.stdout.buffer)

