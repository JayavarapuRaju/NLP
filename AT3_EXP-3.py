import re
text = """Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing"""

while True:
    print("\n------ TEXT SEARCH ENGINE ------")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        result = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
        print("Dates Found:", result)

    elif choice == 2:
        result = re.findall(r'\b[6-9]\d{9}\b', text)
        print("Phone Numbers Found:", result)

    elif choice == 3:
        result = re.findall(r'#\w+', text)
        print("Hashtags Found:", result)

    elif choice == 4:
        result = re.findall(r'@\w+', text)
        print("Mentions Found:", result)

    elif choice == 5:
        prefix = input("Enter Prefix: ")
        pattern = r'\b' + re.escape(prefix) + r'\w*'
        result = re.findall(pattern, text, re.IGNORECASE)
        print("Matching Words:", result)

    elif choice == 6:
        suffix = input("Enter Suffix: ")
        pattern = r'\b\w*' + re.escape(suffix) + r'\b'
        result = re.findall(pattern, text, re.IGNORECASE)
        print("Matching Words:", result)

    elif choice == 7:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
