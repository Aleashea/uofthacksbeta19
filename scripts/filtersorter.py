from queue import PriorityQueue

import nltk
from pymongo import *


uri = 'mongodb://<hinamomori>:<hyacint5>@ds159574.mlab.com:59574/trashset'

client = MongoClient(uri)

db = client.get_database()

def jtos(json):
    res = ""
    for i in json:
        res += i['name']
        res += " "
    return res


def chew(string):
    tokens = nltk.word_tokenize(string)
    tagged = nltk.pos_tag(tokens)
    arr = []
    for (a,b) in tagged:
        if b == "NN":
            arr.append(a)
    return arr


def prioritize(arr, kvset):
    pq = PriorityQueue()
    for i in arr:
        if i in kvset:
            pq.append(PriorityEntry(kvset.get(i), i))
    return pq


def extract(pq):
    if not pq.isEmpty():
        a = pq.delete()
    return a.data



class PriorityEntry(object):

    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
