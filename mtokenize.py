#!/usr/bin/python3

import nltk
import pickle
import sys
import re


if len(sys.argv) > 1:
    if sys.argv[1] != 'cess_esp':
        raise ValueError('Unknown corpus {}'.format(sys.argv[1]))
    tokens = nltk.corpus.cess_esp.words()
else:
    tokens = nltk.tokenize.word_tokenize(sys.stdin.read(), language='spanish')

def simplify(w):
    w = re.sub(r'^\d+$', '<NUM>', w)
    w = re.sub(r'^[IVXLCDM]+$', '<NUM_R>', w)
    return w

tokens = list(map(simplify, tokens))
pickle.dump(tokens, sys.stdout.buffer)

