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

with open ('data/structured/unique.txt', 'w') as f:
    result = (Counter(result).keys())
    result = sorted(result)
    f.writelines('\n'.join(result))
    