from collections import Counter

def count_words(string:str):
    stringList = string.lower().split()
    return Counter(stringList)
