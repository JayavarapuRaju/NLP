words = ["govern", "government", "governance"]

for word in words:

    if word == "govern":
        root = "govern"
        suffix = "-"
        level = "Base"

    elif word.endswith("ment"):
        root = "govern"
        suffix = "ment"
        level = "Level-1"

    elif word.endswith("ance"):
        root = "govern"
        suffix = "ance"
        level = "Level-1"

    print("Original :", word)
    print("Root :", root)
    print("Suffix :", suffix)
    print("Derivation :", level)
    print("Normalized :", root)
    print("----------------------")
#OUTPUT
    Original : govern
Root : govern
Suffix : -
Derivation : Base
Normalized : govern
----------------------
Original : government
Root : govern
Suffix : ment
Derivation : Level-1
Normalized : govern
----------------------
Original : governance
Root : govern
Suffix : ance
Derivation : Level-1
Normalized : govern
----------------------
