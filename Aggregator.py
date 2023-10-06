from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "NLTK is a powerful library for natural language processing."
text = "Machine learning is a (subset) of artificial intelligence."
text = "Apple Inc. was founded by Steve Jobs and Steve Wozniak."
text = "python is a powerful library"
text = """Python is a high-level, general-purpose, and very popular programming language. It is being used in web development, Machine Learning applications, along with all cutting-edge technology in Software Industry.
It is being used by almost all tech-giant companies like – Google, Amazon, Facebook, Instagram, Dropbox, Uber… etc.."""
n = len(text)

Content = """Python is a high-level, general-purpose, and very popular programming language. It is being used in web development, Machine Learning applications, along with all cutting-edge technology in Software Industry.
It is being used by almost all tech-giant companies like – Google, Amazon, Facebook, Instagram, Dropbox, Uber… etc.."""


class Aggregator:
    def __init__(self, Content):
        self.Words = word_tokenize(Content)
        self.PartsOfSpeechTags = pos_tag(self.Words)
        self.POSLength = len(self.PartsOfSpeechTags)

    def AddMore(self, TagIndex):
        CollectiveWord = ""
        while TagIndex < self.POSLength and self.PartsOfSpeechTags[TagIndex][1].startswith("NN"):
            CollectiveWord += (self.PartsOfSpeechTags[TagIndex][0] + " ")
            TagIndex += 1
        return (CollectiveWord, TagIndex)

    def GetSemanticKeywords(self):
        TagIndex = 0
        SemanticWords = []

        while TagIndex < self.POSLength:
            CollectiveWord = ""
            Word, Pos = self.PartsOfSpeechTags[TagIndex]
            if Pos.startswith('JJ'):
                CollectiveWord += Word
                Word, TagIndex = self.AddMore(TagIndex + 1)
                CollectiveWord += (" " + Word)
            elif Pos.startswith("NN"):
                Word, TagIndex = self.AddMore(TagIndex)
                CollectiveWord += (" " + Word)
            else:
                TagIndex += 1
            if CollectiveWord:
                SemanticWords.append(CollectiveWord.strip())

        return SemanticWords

# Output: Keywords of given paragraph with Semantically Grouped Words