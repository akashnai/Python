import string
import json
from difflib import *
    

data = json.load(open("dictionary.json"))


def findWord(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())):
        print("Did you mean %s instead " %get_close_matches(word, data.keys())[0])
        decide = input("Press Y for yes and N for no: ")
        if decide == "y":
            return data[get_close_matches(word,data.keys())[0]] 
        elif decide == "n":
            return("Sorry! Word not found in the dictionary")
        else:
            return("You have entered wrong input")
            
    
    else:
        print("Sorry! Word not found in the dictionary")

word = input("Enter the word you want to search: ")
meaning = findWord(word)

if type(meaning) == list:
    for item in meaning:
        print()
else:
    print(meaning)
