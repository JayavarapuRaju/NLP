# Stemming-Based Preprocessing

words = ["played", "player", "playing"]

print("{:<12} {:<10} {:<12} {:<15} {:<12}".format(
    "Word", "Stem", "Affix", "Type", "Normalized"))

for word in words:

    if word.endswith("ed"):
        stem = word[:-2]
        affix = "-ed"
        mtype = "Inflectional"

    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "-ing"
        mtype = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "-er"
        mtype = "Derivational"

    print("{:<12} {:<10} {:<12} {:<15} {:<12}".format(
        word, stem, affix, mtype, "play"))
#OUTPUT
    Word         Stem       Affix        Type            Normalized  
played       play       -ed          Inflectional    play        
player       play       -er          Derivational    play        
playing      play       -ing         Inflectional    play        

