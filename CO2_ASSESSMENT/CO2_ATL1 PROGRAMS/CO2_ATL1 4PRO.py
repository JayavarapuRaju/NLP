# Finite State Morphological Parser

words = ["writes", "writing", "written"]

print("{:<12} {:<25} {:<15} {:<12} {:<12}".format(
    "Word", "State Transition", "Pattern", "Root", "Normalized"))

for word in words:

    if word == "writes":
        transition = "Start->write->+s->Final"
        pattern = "Regular"
        root = "write"

    elif word == "writing":
        transition = "Start->write->+ing->Final"
        pattern = "Regular"
        root = "write"

    elif word == "written":
        transition = "Start->write->written->Final"
        pattern = "Irregular"
        root = "write"

    print("{:<12} {:<25} {:<15} {:<12} {:<12}".format(
        word, transition, pattern, root, root))
#OUTPUT
    Word         State Transition          Pattern         Root         Normalized  
writes       Start->write->+s->Final   Regular         write        write       
writing      Start->write->+ing->Final Regular         write        write       
written      Start->write->written->Final Irregular       write        write       
