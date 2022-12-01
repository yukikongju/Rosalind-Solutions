#!/usr/bin/python

""" Link: http://rosalind.info/problems/ini2/"""


def getSquaredHypothenuse(a, b):
    return a * a + b * b

if __name__ == "__main__":
    a, b = 933, 971
    squared_hypothenuse = getSquaredHypothenuse(a, b)
    print(squared_hypothenuse)

