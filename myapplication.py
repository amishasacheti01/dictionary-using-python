import json
import difflib
from difflib import get_close_matches

data=json.load(open("076 data.json"))


def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper()in data:
        return data[w.upper()]
        
    else:
        if len(get_close_matches(w,data.keys(),cutoff=0.8))>0:
            print("did u mean '%s' instead?" %get_close_matches(w,data.keys(),cutoff=0.8)[0])
            mean=int(input("enter 1 for yes and 0 for no: "))
            if mean==1:
                return data[get_close_matches(w,data.keys(),cutoff=0.8)[0]]
            elif mean==0:
                return "ohk"
            else:
                return "double check"
        else:
            return "please double check"
        

word=input("enter the word: ")
out=translate(word)

if type(out)==list:
    for i in out:
        print(i)

else:
    print(out)
