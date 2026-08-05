words = ["activate", "activation", "reactivation"]

for word in words:

    prefix = "-"
    suffix = "-"

    if word == "activate":
        root = "activate"
        sequence = "Base"

    elif word == "activation":
        root = "activate"
        suffix = "ion"
        sequence = "activate + ion"

    elif word == "reactivation":
        prefix = "re"
        root = "activate"
        suffix = "ion"
        sequence = "re + activate + ion"

    print("Word :", word)
    print("Prefix :", prefix)
    print("Root :", root)
    print("Suffix :", suffix)
    print("Sequence :", sequence)
    print("Normalized :", root)
    print("------------------------")
#OUTPUT
    Word : activate
Prefix : -
Root : activate
Suffix : -
Sequence : Base
Normalized : activate
------------------------
Word : activation
Prefix : -
Root : activate
Suffix : ion
Sequence : activate + ion
Normalized : activate
------------------------
Word : reactivation
Prefix : re
Root : activate
Suffix : ion
Sequence : re + activate + ion
Normalized : activate
------------------------
