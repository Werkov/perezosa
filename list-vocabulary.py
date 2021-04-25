#!/usr/bin/python3

import nltk
import pickle
import string
import sys

if len(sys.argv) < 2:
    raise ValueError('Expected pickle filename arg')

f = open(sys.argv[1], 'rb')
counter = pickle.load(f)

ignored_words = nltk.corpus.stopwords.words('spanish')
ignored_words.extend(c for c in string.punctuation)
ignored_words.extend(['<num>', '<num_r>'])
ignnored_wors = set(ignored_words)

n = sum(counter.values())
prob = 0.95
cover = 0

for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=True):
    cover += v
    if k.lower() in ignored_words:
        continue
    print(k, v)

    if cover / n > prob:
        break
