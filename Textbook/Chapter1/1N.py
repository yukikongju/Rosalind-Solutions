#!/usr/bin/env python

# https://rosalind.info/problems/ba1n/

#  idea 1: (slow) create all permutations and check if permutations hamming 
#  distance is within d (4^k * n)


def getDNeighborhood(pattern, d):
    # 1. generate all kmers of length k
    kmers = getAllKmersofLengthK(len(pattern))


    # 2. find neighbors
    neighbors = []
    for kmer in kmers:
        if hammingDistance(pattern, kmer) <= d:
            neighbors.append(kmer)

    return '\n'.join(neighbors)

def getAllKmersofLengthK(k):
    """ Find all kmer of length k """
    permutations = []
    findAllKmers(permutations, k, '')
    return permutations

def findAllKmers(permutations, k, v):
    """ 
    Helper method to find all permutations
    param: 
        - permutations: array of all permutations
        - k: length of kmer
        - v: vector to be constructed
    """
    if len(v) == k:
        permutations.append(v)
    else:
        for nuc in ['A', 'C', 'G', 'T']:
            w = v + nuc
            findAllKmers(permutations, k, w)

    
def hammingDistance(text1, text2):
    distance = 0
    for nuc1, nuc2 in zip(text1, text2):
        if nuc1 != nuc2:
            distance += 1
    return distance
    

if __name__ == "__main__":
    #  print(getDNeighborhood('ACG', 1))
    print(getDNeighborhood('TAGTTTGTCAT', 3))
    #  file = 'Textbook/Chapter1/data/rosalind_ba1n.txt'
    #  with open(file, 'r') as f:
    #      string = f.readline().strip()
    #      d = int(f.readline().strip())
    #  print(getDNeighborhood(string, d))

