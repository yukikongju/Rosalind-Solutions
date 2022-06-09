#!/usr/bin/env python

#  https://rosalind.info/problems/ba1l/

# PatternToNumber(AGT) = 4 * PatternToNumber(AG) + SymbolToNumber(T) = 8 + 3 = 11


def patternToNumber(pattern):
    if len(pattern) == 0:
        return 0
    prefix = pattern[0:-1]
    symbol = pattern[-1]        # last number
    return 4*patternToNumber(prefix) + symbolToNumber(symbol)

def symbolToNumber(symbol):
    symbolToNumDict = {'A':0, 'C':1, 'G':2, 'T':3}
    return symbolToNumDict.get(symbol)


if __name__ == "__main__":
    #  print(patternToNumber('GT'))
    print(patternToNumber('AGT'))
