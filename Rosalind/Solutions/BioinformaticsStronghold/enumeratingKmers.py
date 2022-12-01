#!/usr/bin/python

""" Link: http://rosalind.info/problems/lexf/"""


def get_kmers(char_list, n):
    kmers = char_list
    for i in range(1, n):
        temp = []
        for char in char_list:
            for substring in kmers:
                temp.append(char + substring)
        kmers = temp
    return kmers

def printPermutations(permutations):
    for perm in permutations:
        print(perm)

if __name__ == "__main__":
    string = 'A C G T'
    n = 2
    char_list = string.split(' ')
    permutations = get_kmers(char_list, n)
    printPermutations(permutations)
