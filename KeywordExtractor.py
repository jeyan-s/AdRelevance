import string
import nltk
from nltk.corpus import stopwords
from collections import defaultdict as dd 

Sentence = """Python is a high-level, general-purpose, and very popular programming language. It is being used in web development, Machine Learning applications, along with all cutting-edge technology in Software Industry.
It is being used by almost all tech-giant companies like – Google, Amazon, Facebook, Instagram, Dropbox, Uber… etc.."""

Sentence = [y for x in Sentence.split('.') for y in x.split()]
Sentence = ['Python', 'high-level', 'general-purpose', 'popular programming language', 'web development', 'Machine Learning applications', 'cutting-edge technology', 'Software Industry', 'tech-giant companies', '– Google', 'Amazon', 'Facebook', 'Instagram', 'Dropbox', 'Uber…', '..']
Punctuations = string.punctuation

class KeywordExtractor:
    def __init__(self, RequiredKeywordsCount = 10):
        self.Priority = dd(lambda : -1)
        self.Stamp = 1
        self.RequiredKeywordsCount = RequiredKeywordsCount

    def UpdateWords(self, Content):
        New_Content = []
        for x in Content:
            x = x.lower()
            for y in Punctuations:
                x = x.replace(y, "")
            New_Content.append(x)
            if self.Priority[x] == -1:
                self.Priority[x] = self.Stamp 
                self.Stamp += 1
        return New_Content

    def Prioritize(self, Contents):
        Hash = dd(int)
        PartsOfSpeechTags = nltk.pos_tag(Contents)
        for x, y in PartsOfSpeechTags:
            Hash[x] += 1
        return sorted(Hash.items(), key = lambda x: (x[1], -self.Priority[x[0]]), reverse = True)

    def GetRequiredKeywords(self, Content):
        RequiredKeywords = []
        Content = self.UpdateWords(Content)
        Content = self.Prioritize(Content)
        ContentLength = len(Content)
        for x in range(min(ContentLength, self.RequiredKeywordsCount)):
            RequiredKeywords.append(Content[x][0].title())
        return tuple(RequiredKeywords)

# Output: Top 10 Keywords of a Specific URL