#!/usr/bin/python

""" Link: http://rosalind.info/problems/ini6/"""

def getWordDictionariesFromString(string):
    dictionary = {}
    for word in string.split(' '):
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

def printDictionary(dictionary):
    for word, value in dictionary.items():
        print(word, value)

if __name__ == "__main__":
    string = 'We tried list and we tried dicts also we tried Zen' 
    dictionary = getWordDictionariesFromString(string)
    printDictionary(dictionary)
