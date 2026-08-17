"""
Experiment 09: Rule-Based POS Tagger with Regular Expressions
"""
import re

rules = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*s$', 'NNS'),
    (r'.*ly$', 'RB'),
    (r'^\d+$', 'CD'),
    (r'.*', 'NN')
]


def regex_tagger(tokens):
    tagged = []
    for token in tokens:
        for pattern, tag in rules:
            if re.match(pattern, token):
                tagged.append((token, tag))
                break
    return tagged

sentence = 'She quickly finished the tests'
tokens = sentence.split()
print('Sentence:', sentence)
print('Tagged:', regex_tagger(tokens))

# Sample output:
# Tagged: [('She', 'NN'), ('quickly', 'RB'), ('finished', 'VBD'), ('the', 'NN'), ('tests', 'NNS')]
