import json
from difflib import get_close_matches

data  = json.load(open("data.json"))
word = str(input("Enter your word: ")).lower()
def definitionfinder(word):
    if word in data:
        for elem in data[word]:
            print(elem)
    elif word.title() in data:
        word = word.title()
        for elem in data[word]:
            print(elem)
    elif word.upper() in data:
        word = word.upper()
        for elem in data[word]:
            print(elem)
    elif len(get_close_matches(word, data.keys())) > 0:
        possibleword = get_close_matches(word, data.keys())[0]
        print("Did you mean the word %s? Yes[Y] or No[N]?" % possibleword)
        answer = str(input())
        if answer == "Y" or answer == "Yes" or answer == "yes" or answer == "YES" or answer == "y":
            word = possibleword
            for elem in data[word]:
                print(elem)
        elif answer == "N" or answer == "No" or answer == "no" or answer == "NO" or answer == "n":
            print("The word doesn't exist. Please double check your word.")
        else:
            print("Not a valid response.")
    else:
        print("The word doesn't exist. Please double check your word.")


definitionfinder(word)