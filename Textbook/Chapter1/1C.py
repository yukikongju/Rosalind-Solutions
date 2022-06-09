#!/usr/bin/env python

# Problem: https://rosalind.info/problems/ba1c/


def findReverseComplement(dna):
    """ 
    Given: A DNA string Pattern.
    Return: Pattern, the reverse complement of Pattern.
    """
    # 1. create map nucleotides
    nucleotides_map = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

    # 2. reverse = complement + invert
    reverse = []
    for nucleotide in reversed(dna):
        reverse.append(nucleotides_map.get(nucleotide))

    return ''.join(reverse) 


if __name__ == "__main__":
    #  print(findReverseComplement('AAAACCCGGT') == 'ACCGGGTTTT')
    #  print(findReverseComplement('ACACAC') == 'GTGTGT')

    file = 'Textbook/Chapter1/data/rosalind_ba1c_test.txt'
    file = 'Textbook/Chapter1/data/rosalind_ba1c.txt'
    with open(file, 'r') as f:
        dna = f.read().strip()
        reverseDna = findReverseComplement(dna)
        print(reverseDna)
    




