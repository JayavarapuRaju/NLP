from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["relational", "relation", "relate"]

print("{:<15} {:<20} {:<15}".format(
    "Original", "Applied Rule", "Final Stem"))

for word in words:

    if word.endswith("ational"):
        rule = "Remove -ational"

    elif word.endswith("ation"):
        rule = "Remove -ation"

    elif word.endswith("ate"):
        rule = "Remove -ate"

    else:
        rule = "Porter Rule"

    stem = ps.stem(word)

    print("{:<15} {:<20} {:<15}".format(
        word, rule, stem))
