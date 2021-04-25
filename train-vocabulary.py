#!/usr/bin/python3

import pickle
import sys
from collections import Counter

if len(sys.argv) < 2:
    raise ValueError('Expected pickle filename arg')

f = open(sys.argv[1], 'rb')
tokens = pickle.load(f)

counter = Counter(tokens)

pickle.dump(counter, sys.stdout.buffer)
