#/usr/bin/python3
import json 
import difflib
from difflib import SequenceMatcher

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "Uh oh! I don't think that word exists!"

word = input("Enter word: ")

print(translate(word))

