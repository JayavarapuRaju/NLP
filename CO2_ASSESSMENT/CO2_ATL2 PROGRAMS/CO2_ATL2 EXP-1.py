words = ["analyzing", "analysis", "analytical"]

for word in words:
    root = "analyze"

    if word.endswith("ing"):
        suffix = "ing"
        mtype = "Inflectional"
    elif word.endswith("sis"):
        suffix = "sis"
        mtype = "Derivational"
    elif word.endswith("ical"):
        suffix = "ical"
        mtype = "Derivational"
    else:
        suffix = "-"
        mtype = "Base"

    print("Original Word :", word)
    print("Root :", root)
    print("Affix :", suffix)
    print("Type :", mtype)
    print("Normalized :", root)
    print("------------------------")

    #OUTPUTOriginal Word : analyzing
Root : analyze
Affix : ing
Type : Inflectional
Normalized : analyze
------------------------
Original Word : analysis
Root : analyze
Affix : sis
Type : Derivational
Normalized : analyze
------------------------
Original Word : analytical
Root : analyze
Affix : ical
Type : Derivational
Normalized : analyze
------------------------
