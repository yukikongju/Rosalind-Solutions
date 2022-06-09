#!/usr/bin/env python

#  https://rosalind.info/problems/ba1e/

def findClumpsInPattern(genome, k, L, t):
    """ 
    Given: A string Genome, and integers k, L, and t.
    Return: All distinct k-mers forming (L, t)-clumps in Genome.
    (all kmers of length k that occurs at least t times)
    """
    clumps = []
    for i in range(len(genome) - L + 1):
        window = genome[i:i+L]
        freqMap = getFreqTable(genome, k)
        for key, value in freqMap.items():
            if value >= t:
                clumps.append(key)

    clumps = list(dict.fromkeys(clumps))      # drop dupplicates in list

    return ' '.join(clumps)

    
def getFreqTable(dna, k):
    """ 
    Given: dna string, integer k
    Return: table of all kmers count
    """
    kmers_count = {}
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i+k]
        if kmer not in kmers_count:
            kmers_count[kmer] = 1
        else: 
            kmers_count[kmer] += 1
    return kmers_count

    
if __name__ == "__main__":
    genome = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
    k, L, t = 5, 75, 4
    print(findClumpsInPattern(genome, k, L, t))


    #  file = 'Textbook/Chapter1/data/rosalind_ba1e_test1.txt'
    file = 'Textbook/Chapter1/data/rosalind_ba1e.txt'
    with open(file, 'r') as f:
        genome = f.readline().strip()
        k, L, t = f.readline().split(' ')
        print(findClumpsInPattern(genome, int(k), int(L), int(t)))

    



    
