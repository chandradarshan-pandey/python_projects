import json
from difflib import get_close_matches
data = json.load(open("076 data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]# if user entered "texas" this will check for "Texas" as well
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead..! Enter y for yes and n for no :" %  get_close_matches(w,data.keys())[0])
        if yn == "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "n":
            return " We didn't underrstand your query."
        else:
            return "The word doesn't exist"
    else:
        return "The word doesn't exist try again"
word=input("enter a word:")

output = translate(word)

if type(output)==list:
    for items in output:
        print(items)
else:
    print(output)
