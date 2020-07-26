#!/usr/bin/python

from itertools import permutations

def genePermutations(num):
    count = 0
    permutations_list = list(permutations(range(1, num + 1)))
    return len(permutations_list), permutations_list

def printPermutationsList(permutations_list):
    for perm in permutation_list:
        print(' '.join(map(str, perm)))

if __name__ == "__main__":
    num = 7
    count, permutation_list = genePermutations(num)
    print(count)
    printPermutationsList(permutation_list)

