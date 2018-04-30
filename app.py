#/usr/bin/python3
import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        if len(get_close_matches(w, data.keys())) > 0:
            closest_match = get_close_matches(w, data.keys())[0]
            yes_or_no = input("Did you mean " + closest_match + " instead? Enter Y if yes, or N if no.")
            if yes_or_no == "Y":
                return data[closest_match]
            elif yes_or_no == "N":
                return "Uh oh! I don't think that word exists!"
            else:
                return "Whoops! I didn't understand your answer."
        else: 
            return "Uh oh! I don't think that word exists!"

word = input("Enter word: ")

print(translate(word))

