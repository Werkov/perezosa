#!/usr/bin/python3

import nltk
import pickle
import sys

if len(sys.argv) < 2:
    raise ValueError('Expected pickle filename arg')

f = open(sys.argv[1], 'rb')
finder = pickle.load(f)

# TODO support generic ngram
bigram_measures = nltk.collocations.BigramAssocMeasures()
best = finder.nbest(bigram_measures.pmi, 20)  
print(best)
