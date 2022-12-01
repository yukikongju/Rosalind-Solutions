#!/usr/bin/env python

#  https://rosalind.info/problems/ba1m/
# Problem: doesn't work when k>4 because dict is 
# not appropriate (modulo are not all mapped)

def numberToPattern(n, k):
    #  print(n,k)
    if n == 0: 
        return numberToSymbol(n)
    quotient = n // k
    remainder = n % k
    symbol = numberToSymbol(remainder)
    print(symbol)
    return numberToPattern(quotient, k) + symbol

    
def numberToSymbol(index):
    symbols_dict = {0: 'A', 1:'C', 2: 'G', 3: 'T'}
    index = index % 4
    return symbols_dict.get(index)
    

if __name__ == "__main__":
    #  print(numberToPattern(9904, 4))
    #  print(numberToPattern(45, 4))
    #  print(numberToPattern(5186, 8))
    print(numberToPattern(5862, 10))




