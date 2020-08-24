import json
from difflib import get_close_matches

data = json.load(open("D:\Code\Python\Dictionary\original.json"))

def find(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word , data.keys())) > 0:
        print("Do you mean %s instead" %get_close_matches(word , data.keys())[0])
        decide = input("Press y for yes or n for no: ")
        decide = decide.lower()

        if decide == 'y':
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == 'n':
            return "Your Word has no Meaning."
        else:
            return "Please Enter valid keyword."

    else:
        return ("Your Word has no Meaning.")


word = input("Enter the word you want to search: ")

output = find(word)

if type(output) == list:
    for item in output:
        print(item)
else: 
    print(output)