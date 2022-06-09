#!/usr/bin/env python

#  https://rosalind.info/problems/ba1g/
# alternative solution: distance = sum(1 for i, j in zip(dna1, dna2) if i != j)

def hammingDistance(dna1, dna2):
    """ 
    Given: Two DNA strings.
    Return: An integer value representing the Hamming distance.
    """
    # 1. base case: string not same length
    if len(dna1) != len(dna2):
        return -1

    # 2. calculate hamming distance
    dist = 0
    for p,q in zip(dna1, dna2):
        if p != q:
            dist += 1
    return dist

if __name__ == "__main__":
    print(hammingDistance('GGGCCGTTGGT', 'GGACCGTTGAC') == 3)    

    #  file = 'Textbook/Chapter1/data/rosalind_ba1g_test6.txt'
    file = 'Textbook/Chapter1/data/rosalind_ba1g.txt'
    with open(file, 'r') as f:
        dna1 = f.readline().strip()
        dna2 = f.readline().strip()
        print(hammingDistance(dna1, dna2))
            
