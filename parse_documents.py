import string
import re
document_path = "data/unstructured/1.xml"
f = open(document_path, "r", encoding="utf8")
result = []
n = 0

for line in f:
    l_begin = "<l"
    l_end = "</l>"
    if l_begin in line and l_end in line:
        line = re.sub('<[^<]+>', "", line)
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.replace("\n", "")
        line = line.lower()
        line = "<BOS>" + " " +  line + " " + "<EOS>" + " "
        result.append(line)

for i in range(0, len(result), 150):
    n += 1
    chunk = result[i:i + 150]
    with open("data/structured/section" + str(n) + ".txt", 'w') as out_file:
        out_file.writelines(chunk)
    

print (result[:5])