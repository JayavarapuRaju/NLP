words = ["disagree", "agreement", "agreeable"]

for word in words:
    prefix = "-"
    suffix = "-"

    if word.startswith("dis"):
        prefix = "dis"
        root = "agree"
        category = "Derivational"
        meaning = "Negative meaning"

    elif word.endswith("ment"):
        root = "agree"
        suffix = "ment"
        category = "Derivational"
        meaning = "Action/Result"

    elif word.endswith("able"):
        root = "agree"
        suffix = "able"
        category = "Derivational"
        meaning = "Capability"

    print("Word :", word)
    print("Prefix :", prefix)
    print("Root :", root)
    print("Suffix :", suffix)
    print("Category :", category)
    print("Meaning :", meaning)
    print("Normalized :", root)
    print("------------------------")
#OUTPUT
    Word : disagree
Prefix : dis
Root : agree
Suffix : -
Category : Derivational
Meaning : Negative meaning
Normalized : agree
------------------------
Word : agreement
Prefix : -
Root : agree
Suffix : ment
Category : Derivational
Meaning : Action/Result
Normalized : agree
------------------------
Word : agreeable
Prefix : -
Root : agree
Suffix : able
Category : Derivational
Meaning : Capability
Normalized : agree
---------------------
