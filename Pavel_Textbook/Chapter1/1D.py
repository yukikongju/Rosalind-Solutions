#!/usr/bin/env python

# https://rosalind.info/problems/ba1d/

def findAllOccurencesOfPattern(pattern, dna):
    """ 
    Given: Strings Pattern and Genome.
    Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing.
    """
    #  print(pattern, dna)
    indexes = []
    for i in range(len(dna) - len(pattern) + 1):
        substring = dna[i: i+ len(pattern)]
        print(substring)
        if substring == pattern:
            indexes.append(i)

    print(indexes)
    #  return ' '.join(indexes)
    return indexes
    

if __name__ == "__main__":
    #  print(findAllOccurencesOfPattern('ATAT', 'GATATATGCATATACTT'))

    file = 'Textbook/Chapter1/data/rosalind_ba1d_test.txt'
    #  file = 'Textbook/Chapter1/data/rosalind_ba1d.txt'
    with open(file, 'r') as f:
        pattern = f.read().strip()
        dna = f.read().strip()
        print(pattern, dna)
        print(findAllOccurencesOfPattern(pattern, dna))


