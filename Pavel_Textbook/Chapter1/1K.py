#!/usr/bin/env python

#  https://rosalind.info/problems/ba1k/

from itertools import permutations


def findFrequencyArray(text, k):
    """ 
    Given: A DNA string Text and an integer k.
    Return: The frequency array of k-mers in Text.
    """

    # 1. generate all kmers in lexicographical order
    perms = findPermutationsKmers(k)

    # 2. initialize dict_count for all kmers permutations to zero
    dict_count = {}
    for perm in perms:
        dict_count[perm] = 0

    # 3. get occurence count for all kmers in text
    for i in range(len(text) - k +1):
        substring = text[i:i+k]
        dict_count[substring] += 1


    # 4. sort kmer in lexicographic order
    frequency_array = []
    for kmer, count in sorted(dict_count.items()):
        frequency_array.append(str(count))

    return ' '.join(frequency_array)


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
    text = 'ACGCGGCTCTGAAA'
    k = 2
    #  print(findFrequencyArray(text, k))

    perms = findPermutationsKmers(2)
    print(perms[11])



    file = "Textbook/Chapter1/data/rosalind_ba1k_test3.txt"
    file = "Textbook/Chapter1/data/rosalind_ba1k_test5.txt"
    #  file = "Textbook/Chapter1/data/rosalind_ba1k.txt"
    #  with open(file, 'r') as f:
    #      text = f.readline().strip()
    #      k = int(f.readline().strip())
    #      print(findFrequencyArray(text, k))



