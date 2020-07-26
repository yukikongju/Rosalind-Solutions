#!/usr/bin/python

""" Link: http://rosalind.info/problems/ini4/"""

def getSumOddIntegers(num1, num2):
    total = 0
    for num in range(num1, num2):
        if num % 2 == 1:
            total += num
    return total


if __name__ == "__main__":
    a, b = 4851, 9736
    sumOfOddsIntegers = getSumOddIntegers(a, b)
    print(sumOfOddsIntegers)
