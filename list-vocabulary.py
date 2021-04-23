#!/usr/bin/python3

import pickle
import sys

if len(sys.argv) < 2:
    raise ValueError('Expected pickle filename arg')

f = open(sys.argv[1], 'rb')
counter = pickle.load(f)


for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=True):
    print(k, v)
