#!/usr/bin/python

""" Link : http://rosalind.info/problems/fibo/"""

def getFibonacciNumber(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return getFibonacciNumber(n - 1) + getFibonacciNumber(n - 2)

if __name__ == "__main__":
    n = 22
    fibonacci = getFibonacciNumber(n)
    print(fibonacci)
