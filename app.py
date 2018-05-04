#/usr/bin/python3
import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

def no_match():
  return "Uh oh! I don't think that word exists!"

def error():
  return "Whoops! I didn't understand your answer."

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    else:
        if len(get_close_matches(w, data.keys())) > 0:
            closest_match = get_close_matches(w, data.keys())[0]
            yes_or_no = input("Did you mean " + closest_match + " instead? Enter Y if yes, or N if no.")
            if yes_or_no == "Y":
                return data[closest_match]
            elif yes_or_no == "N":
                return no_match()
            else:
                return error()
        else: 
            return no_match()

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for definition in output:
        print(definition)
else:
    print(output)

