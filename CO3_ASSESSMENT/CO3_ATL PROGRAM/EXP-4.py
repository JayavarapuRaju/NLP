import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')

# Rule-Based POS Tagger
def rule_based_pos(sentence):
    tokens = nltk.word_tokenize(sentence)
    tags = []
    for word in tokens:
        if word.lower() in ["the","a","an"]:
            tags.append((word,"DET"))
        elif re.match(r".*ing$", word):
            tags.append((word,"VBG"))
        elif word.lower() in ["is","am","are"]:
            tags.append((word,"VERB"))
        else:
            tags.append((word,"NOUN"))
    return tags

# Stochastic POS Tagger (using NLTK pretrained)
def stochastic_pos(sentence):
    tokens = nltk.word_tokenize(sentence)
    return nltk.pos_tag(tokens, tagset="universal")

# Transformation-Based Tagging (simple correction rules)
def transform_based(tags):
    corrected = []
    for i,(word,tag) in enumerate(tags):
        if tag=="NOUN" and i>0 and tags[i-1][1]=="PRON":
            corrected.append((word,"VERB"))
        else:
            corrected.append((word,tag))
    return corrected

# Example
sentence = "The student is playing football"
print("Rule-Based:", rule_based_pos(sentence))
print("Stochastic:", stochastic_pos(sentence))
print("Transformation-Based:", transform_based(rule_based_pos(sentence)))
