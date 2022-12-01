#!/usr/bin/python
import this
""" Link: http://rosalind.info/problems/ini2/"""


def getSquaredHypothenuse(a, b):
    return a * a + b * b

if __name__ == "__main__":
    a, b = 3, 5
    squared_hypothenuse = getSquaredHypothenuse(a, b)
    print(squared_hypothenuse)

