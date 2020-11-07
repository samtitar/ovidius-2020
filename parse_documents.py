import string
import re
document_path = "data/unstructured/1.xml"
f = open(document_path, "r", encoding="utf8")
result = []

for line in f:
    l_begin = "<l"
    l_end = "</l>"
    if l_begin in line and l_end in line:
        line = re.sub('<[^<]+>', "", line)
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.replace("\n", "")
        line = line.lower()
        result.append(line)

print (result[:20])