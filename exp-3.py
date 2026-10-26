from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "plays",
         "happily", "studies"]

for word in words:
    root = stemmer.stem(word)
    print(word, "->", root)
