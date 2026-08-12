class BackoffModel:
    def __init__(self, corpus):
        self.unigram = NGramModel(corpus, 1)
        self.bigram = NGramModel(corpus, 2)
        self.trigram = NGramModel(corpus, 3)

    def backoff_prob(self, context, word):
        trigram_context = tuple(context[-2:])
        bigram_context = tuple(context[-1:])
        if self.trigram.prob(trigram_context, word) > 0:
            return self.trigram.prob(trigram_context, word)
        elif self.bigram.prob(bigram_context, word) > 0:
            return self.bigram.prob(bigram_context, word)
        else:
            return self.unigram.prob((), word)

    def deleted_interpolation(self, context, word, lambdas=(0.2,0.3,0.5)):
        trigram_context = tuple(context[-2:])
        bigram_context = tuple(context[-1:])
        p1 = self.unigram.prob((), word)
        p2 = self.bigram.prob(bigram_context, word)
        p3 = self.trigram.prob(trigram_context, word)
        return lambdas[0]*p1 + lambdas[1]*p2 + lambdas[2]*p3

# Example
bm = BackoffModel(corpus)
print("Backoff prob:", bm.backoff_prob(["the","student","is"], "playing"))
print("Deleted interpolation:", bm.deleted_interpolation(["the","student","is"], "playing"))
