#!/usr/bin/env python

#  https://rosalind.info/problems/ba1h/

def findApproximatePatternMatchingProblem(pattern, dna, d):
    """ 
    Given: Strings Pattern and Text along with an integer d.
    Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
    """
    indices = []
    print(len(dna), len(pattern))
    for i in range(len(dna) - len(pattern) + 1):
        substring = dna[i: i + len(pattern)]
        dist = hammingDistance(substring, pattern)
        if dist <= d:
            indices.append(str(i))

    return ' '.join(indices)
    

def hammingDistance(dna1, dna2):
    distance = sum(1 for i, j in zip(dna1, dna2) if i != j)
    return distance


if __name__ == "__main__":
    pattern = 'ATTCTGGA'
    dna = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC'
    d = 3

    #  print(findApproximatePatternMatchingProblem(pattern, dna, d))

    file = 'Textbook/Chapter1/data/rosalind_ba1h_test6.txt'
    #  file = 'Textbook/Chapter1/data/rosalind_ba1h.txt'
    with open(file, 'r') as f:
        pattern = f.readline().strip()
        dna = f.readline().strip()
        d = int(f.readline().strip())
        #  print(dna, pattern, d)
        print(findApproximatePatternMatchingProblem(pattern, dna, d))


