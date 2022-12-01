#!/usr/bin/python

""" Link: http://rosalind.info/problems/fib/ """

def getNumberRabbits(n, k):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return getNumberRabbits(n - 1, k) + k * getNumberRabbits(n - 2, k)

if __name__ == "__main__":
    n = 29
    k = 3
    rabbits = getNumberRabbits(n, k)
    print(rabbits)


