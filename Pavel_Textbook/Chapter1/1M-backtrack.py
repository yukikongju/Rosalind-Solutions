#!/usr/bin/env python

#  https://rosalind.info/problems/ba1m/

#  https://rosalind.info/problems/ba1l/


def NumberToPattern(n, k):
    """ 
    Given: nth kmer pattern and the length k of the kmer 
    Return: the kmer
    """
    # generate all permutations in lexicographical order
    perms = findPermutationsKmers(k)
    return perms[n]


def findPermutationsKmers(n):
    """ 
    Given: length of kmer n
    Return: list of all kmers permutations of length n
    Ex: k=2 => 'AA', 'AT', 'AC', 'AG', ..., 'TT'
    """
    permutations = []
    backtrackKmerPermutations(n, '', permutations)
    return permutations


def backtrackKmerPermutations(n, vect, permutations):
    """ 
    helper method to find all permutations
    """
    # backtracking algorithm
    if len(vect) == n:
        permutations.append(vect)
    else:
        for nuc in ['A', 'C', 'G', 'T']:
            w = f"{vect}{nuc}"
            backtrackKmerPermutations(n, w, permutations)

if __name__ == "__main__":
    print(NumberToPattern(11, 2) == 'GT')


