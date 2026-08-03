# Morphological Parsing Module

words = ["unhappy", "happiness", "happily"]

print("{:<12} {:<10} {:<10} {:<10} {:<15} {:<10}".format(
    "Word", "Prefix", "Root", "Suffix", "Type", "Normalized"))

for word in words:

    if word.startswith("un"):
        prefix = "un-"
        root = "happy"
        suffix = "-"
        mtype = "Derivational"

    elif word.endswith("ness"):
        prefix = "-"
        root = "happy"
        suffix = "-ness"
        mtype = "Derivational"

    elif word.endswith("ly"):
        prefix = "-"
        root = "happy"
        suffix = "-ly"
        mtype = "Derivational"

    print("{:<12} {:<10} {:<10} {:<10} {:<15} {:<10}".format(
        word, prefix, root, suffix, mtype, "happy"))
#OUTPUT
    Word         Prefix     Root       Suffix     Type            Normalized
unhappy      un-        happy      -          Derivational    happy     
happiness    -          happy      -ness      Derivational    happy     
happily      -          happy      -ly        Derivational    happy  
