import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, word_tokenize

# Download required resources (only needed once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Sample text
text = "The children are playing happily in the garden."

# Tokenize text
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Part-of-speech tagging
pos_tags = pos_tag(tokens)
print("POS Tags:", pos_tags)

# Stemming
stemmer = PorterStemmer()
stems = [stemmer.stem(word) for word in tokens]
print("Stems:", stems)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(word) for word in tokens]
print("Lemmas:", lemmas)


