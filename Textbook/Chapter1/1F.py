#!/usr/bin/env python

# Problem: https://rosalind.info/problems/ba1f/

def findMinSkewIndex(dna):
    """ 
    Given: A DNA string Genome.
    Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).
    """
    # 1. create differences array: count difference: +1 if 'C', -1 if 'G'
    differences = [0]*len(dna)
    count = 0
    values = {'A':0,'T':0,'C':-1,'G':1}
    for i, nuc in enumerate(dna):
        differences[i] = count
        count += values[nuc]

    # 2. find min skew value in absolute value
    min_skew = min(differences)

    # 3. find index with min_skew
    indices = [str(i) for i, diff in enumerate(differences) if diff == min_skew]
    return ' '.join(indices)

if __name__ == "__main__":
    #  print(findMinSkewIndex('CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG'))
    #  print(findMinSkewIndex('ACCG'))
    #  print(findMinSkewIndex('ACCC'))
    #  print(findMinSkewIndex('CCGGGT'))
    #  print(findMinSkewIndex('CCGGCCGG'))
    file = 'Textbook/Chapter1/data/rosalind_ba1f_test.txt'
    file = 'Textbook/Chapter1/data/rosalind_ba1f.txt'
    with open(file) as f:
        dna = f.readline().strip()
        print(findMinSkewIndex(dna))
    
