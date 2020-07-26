#!/usr/bin/python

""" Link: http://rosalind.info/problems/pper/"""

def get_partial_permutations(n, k):
    count = 1
    for i in range(k):
        count *= (n - i)
    return count % 1000000

if __name__ == "__main__":
    n = 86     # num objects
    k = 9       # num objects taken
    partial_permutations = get_partial_permutations(n, k) 
    print(partial_permutations)
