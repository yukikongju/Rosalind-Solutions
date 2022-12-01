#!/usr/bin/env python

#  https://rosalind.info/problems/ba1b/

# solution: create dictionary of kmers counts

def findMostFrequent(dna, k):
    """ 
    Given: A DNA string Text and an integer k.
    Return: All most frequent k-mers in Text (in any order).
    """
    # 1. count occurence of each kmers in dna
    dict_count = {}
    for i in range(len(dna) - k + 1):
        substring = dna[i:i+k]
        if substring in dict_count.keys():
            dict_count[substring] += 1
        else: 
            dict_count[substring] = 1

    # 2. find biggest values
    max_val = 0
    for val in dict_count.values():
        max_val = max(max_val, val)

    # 3. find all kmers with biggest occurences
    kmers = []
    for key, value in dict_count.items():
        if value == max_val:
            kmers.append(key)

    return kmers


if __name__ == "__main__":
    #  print(findMostFrequent('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4))
    kmers = findMostFrequent('GTCTTACACGTCAACGTCTTACACCCTCCACCCTCCATGCAATAGTAGCTAGTTAGCTAGTTCCCTCCACGTCAACAGCTAGTTGTCTTACACCCTCCACGTCAACGTCTTACACGTCAACAGCTAGTTAGCTAGTTCCCTCCACGTCAACCCCTCCATGCAATAGTCGTCAACTGCAATAGTGTCTTACAAGCTAGTTCCCTCCACCCTCCAAGCTAGTTCGTCAACGTCTTACAAGCTAGTTAGCTAGTTAGCTAGTTAGCTAGTTAGCTAGTTCCCTCCACGTCAACAGCTAGTTTGCAATAGTTGCAATAGTAGCTAGTTCGTCAACCCCTCCATGCAATAGTTGCAATAGTTGCAATAGTCGTCAACGTCTTACAAGCTAGTTAGCTAGTTCCCTCCATGCAATAGTCGTCAACCGTCAACTGCAATAGTGTCTTACACCCTCCACGTCAACTGCAATAGTGTCTTACATGCAATAGTGTCTTACACGTCAACCGTCAACCCCTCCACGTCAACAGCTAGTTTGCAATAGTCGTCAACTGCAATAGTCGTCAACAGCTAGTTTGCAATAGTGTCTTACATGCAATAGTCGTCAACCGTCAACGTCTTACACGTCAACGTCTTACATGCAATAGTTGCAATAGTTGCAATAGTCCCTCCATGCAATAGTCGTCAACGTCTTACATGCAATAGTAGCTAGTTCCCTCCAGTCTTACATGCAATAGTGTCTTACAGTCTTACATGCAATAGTGTCTTACATGCAATAGTGTCTTACATGCAATAGTAGCTAGTTCCCTCCACGTCAACTGCAATAGTCCCTCCATGCAATAGTAGCTAGTT', 12)
    for kmer in kmers:
        print(kmer, end=" ")

    


