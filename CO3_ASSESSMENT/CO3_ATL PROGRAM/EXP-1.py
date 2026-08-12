import re
import math
from collections import defaultdict, Counter
import nltk
nltk.download('punkt')

class NGramModel:
    def __init__(self, corpus, N=2):
        self.N = N
        self.tokens = self.preprocess(corpus)
        self.ngram_counts = defaultdict(Counter)
        self.build_model()

    def preprocess(self, text):
        text = text.lower()
        return nltk.word_tokenize(text)

    def build_model(self):
        for i in range(len(self.tokens) - self.N + 1):
            context = tuple(self.tokens[i:i+self.N-1])
            word = self.tokens[i+self.N-1]
            self.ngram_counts[context][word] += 1

    def prob(self, context, word):
        context_counts = self.ngram_counts[context]
        total = sum(context_counts.values())
        return context_counts[word] / total if total > 0 else 0

    def predict_next(self, context, top_k=5):
        context = tuple(context[-(self.N-1):])
        candidates = self.ngram_counts[context]
        probs = {w: self.prob(context, w) for w in candidates}
        return sorted(probs.items(), key=lambda x: -x[1])[:top_k]

# Example
corpus = "The student is studying. The student is playing. The teacher is teaching."
model = NGramModel(corpus, N=3)
print("Predictions:", model.predict_next(["the", "student", "is"]))
