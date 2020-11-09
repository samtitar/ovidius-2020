import argparse
import os, os.path
from collections import Counter

result = []

documents = os.listdir('data/structured/lemmas/')
for document in documents:
    with open('data/structured/lemmas/' + document, 'r', encoding = 'utf8') as f:
        line = f.readline()
        lemmas = line.split()
        unique = Counter(lemmas).keys()
        result += unique

with open('data/structured/voacb_lemma.txt', 'w') as f:
    result = sorted(Counter(result).keys())
    f.writelines('\n'.join(result))
    