from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "running", "runner",
         "studies", "studying", "happiness", "fishing"]

print("Original Word --> Stemmed Word\n")

for word in words:
    print(word, "-->", ps.stem(word))
