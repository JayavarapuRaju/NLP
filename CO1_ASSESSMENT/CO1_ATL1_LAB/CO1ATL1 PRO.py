import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')
words = ["running", "played", "better", "cars", "studies"]
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
print("Word\t\tStem\t\tLemma")
for word in words:
 stem = stemmer.stem(word)
 lemma = lemmatizer.lemmatize(word)
 print(word, "\t", stem, "\t\t", lemma)
