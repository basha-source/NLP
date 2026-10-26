from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = [
    "playing",
    "running",
    "connected",
    "connection",
    "happiness",
    "studies"
]

print("Original Word -> Stemmed Word")

for word in words:
    print(word, "->", stemmer.stem(word))
