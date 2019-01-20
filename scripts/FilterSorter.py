
import json
import nltk


def jsonstringify(json):
    res = ""
    for i in json:
        res += i['name']
        res += " "
    return res

def