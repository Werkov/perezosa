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
ignored_words.extend(['==', '``', "''", '»', '«', '“'])
ignored_words = set(ignored_words)

n = sum(counter.values())
level_p = [0.5, 0.8, 0.9, 0.95, 0.99]
level_cnt = dict()
vocabs = 0
i = 0
cover = 0

for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=True):
    cover += v
    vocabs += 1
    if k.lower() in ignored_words:
        continue
    print(k, v)

    if i < len(level_p) and cover / n > level_p[i]:
        level_cnt[level_p[i]] = vocabs
        i += 1

level_cnt[1.0] = vocabs


for k, v in sorted(level_cnt.items(), key=lambda x: x[0]):
    print("# {}\t{}".format(k, v))

cover = 0
for w in ignored_words:
    cover += counter[w]
print("# ignored words\t{}".format(cover / n))
