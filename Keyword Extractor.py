import string
import nltk
from nltk.corpus import stopwords
from collections import defaultdict as dd 

Sentence = """Python is a high-level, general-purpose, and very popular programming language. It is being used in web development, Machine Learning applications, along with all cutting-edge technology in Software Industry.
It is being used by almost all tech-giant companies like – Google, Amazon, Facebook, Instagram, Dropbox, Uber… etc.."""

Sentence = [y for x in Sentence.split('.') for y in x.split()]
n = len(Sentence)
Punctuations = string.punctuation
New_Sentence = []
Priority = dd(lambda : -1)
Stamp = 1
RequiredKeywords = 10

for x in Sentence:
    x = x.lower()
    for y in Punctuations:
        x = x.replace(y, "")
    if x not in stopwords.words('english'):
        New_Sentence.append(x)
        if Priority[x] == -1:
            Priority[x] = Stamp 
            Stamp += 1

Hash = dd(int)
New_Sentence = nltk.pos_tag(New_Sentence)
for x, y in New_Sentence:
    if y[:2] == "NN":
        Hash[x] += 1

print("----------------")
# print(Hash)

lst = sorted(Hash.items(), key = lambda x: (x[1], -Priority[x[0]]), reverse = True)
# print(lst)

for x in range(RequiredKeywords):
    print(lst[x][0])