import argparse
import string
import re

import os, os.path

from cltk.lemmatize.latin.backoff import BackoffLatinLemmatizer

L_OPEN = '<l'
L_CLOSE = '</l>'
LB_OPEN = '<lb'

S_DATA_PATH = 'data/structured/'
C_SIZE = 150

parser = argparse.ArgumentParser(description='Parse unstructered documents.')
parser.add_argument('--document', required=True, help='Path to document to parse.')
args = parser.parse_args()

lemmatizer = BackoffLatinLemmatizer()
lemmas_result, tokens_result = [], []

def tokenize(line):
    line = re.sub('<note[^<]+note>', '', line)
    line = re.sub('<[^<]+>', '', line)
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.replace('\n', '')
    line = line.replace('-', '')
    line = line.replace('—', '')
    line = line.replace('“', '')
    line = line.replace('”', '')
    line = line.lower()
    return line.split()

with open(args.document, 'r', encoding='utf8') as f:
    for line in f:
        if (L_OPEN in line and L_CLOSE in line) or LB_OPEN in line:
            tokens = tokenize(line)
            if tokens != []:
                lemmas = lemmatizer.lemmatize(tokens)
                lemmas = list(zip(*lemmas))[1]
                lemma_str = "<BOS>" + " " + ' '.join(lemmas) + " " + "<EOS>" + " "
                line_str = "<BOS>" + " " +  line + " " + "<EOS>" + " "

                lemmas_result.append(lemma_str)
                tokens_result.append(line_str)

doc_start = len(os.listdir(S_DATA_PATH + 'lemmas/'))
print(doc_start)
for i in range(0, len(lemmas_result), C_SIZE):
    doc_name = str(doc_start + i // C_SIZE) + ".txt"
    with open(S_DATA_PATH + "lemmas/section" + doc_name, 'w') as out_file:
        out_file.writelines(lemmas_result[i:i + C_SIZE])
    with open(S_DATA_PATH + "tokens/section" + doc_name, 'w') as out_file:
        out_file.writelines(tokens_result[i:i + C_SIZE])
