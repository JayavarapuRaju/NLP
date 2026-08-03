# Morphological Analysis Pipeline

words = ["connected", "connecting", "connection"]

print("{:<12} {:<10} {:<12} {:<15} {:<12}".format(
    "Word", "Root", "Suffix", "Type", "Normalized"))

for word in words:
    if word.endswith("ed"):
        root = word[:-2]
        suffix = "-ed"
        mtype = "Inflectional"
        normalized = "connect"

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "-ing"
        mtype = "Inflectional"
        normalized = "connect"

    elif word.endswith("ion"):
        root = word[:-3]
        suffix = "-ion"
        mtype = "Derivational"
        normalized = "connect"

    print("{:<12} {:<10} {:<12} {:<15} {:<12}".format(
        word, root, suffix, mtype, normalized))
#OUTPUT
    Word         Root       Suffix       Type            Normalized  
connected    connect    -ed          Inflectional    connect     
connecting   connect    -ing         Inflectional    connect     
connection   connect    -ion         Derivational    connect     

