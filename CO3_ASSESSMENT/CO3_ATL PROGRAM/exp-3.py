def entropy(model, test_tokens, N=2):
    H = 0
    for i in range(len(test_tokens)-N+1):
        context = tuple(test_tokens[i:i+N-1])
        word = test_tokens[i+N-1]
        p = model.prob(context, word)
        if p > 0:
            H += -math.log2(p)
    return H / (len(test_tokens)-N+1)

train = "The student is studying. The teacher is teaching."
test = "The student is learning."
train_model = NGramModel(train, N=2)
test_tokens = nltk.word_tokenize(test.lower())
print("Entropy:", entropy(train_model, test_tokens, N=2))
5
