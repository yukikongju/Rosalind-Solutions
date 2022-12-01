#!/usr/bin/env python

#  https://rosalind.info/problems/ba1i/

def findFrequentWordsWithMismatches(text, k, d):
    """ 
    Given: A string Text as well as integers k and d.
    Return: All most frequent k-mers with up to d mismatches in Text.
    """
    # 1. count approximate pattern count for all kmer in text
    kmers = {}
    for i in range(len(text) - k + 1):
        substring = text[i:i+k]
        if substring not in kmers:
            count = countApproximatePatternMatchingInString(substring, text, d)
            kmers[substring] = count

    # 2. find max_count
    max_count = max(kmers.values())

    # 3. find all kmers with max count
    patterns = []
    for kmer, count in kmers.items():
        if count == max_count:
            patterns.append(kmer)

    return ' '.join(patterns) 

    
def countApproximatePatternMatchingInString(pattern, dna, d):
    """ 
    Given: Strings Pattern and Text along with an integer d.
    Return: Count number of substring of Text with at most d mismatches.
    """
    count = 0
    for i in range(len(dna) - len(pattern) + 1):
        substring = dna[i: i + len(pattern)]
        dist = hammingDistance(substring, pattern)
        if dist <= d:
            count += 1
    return count

def hammingDistance(dna1, dna2):
    return sum(1 for i, j in zip(dna1, dna2) if i != j)


if __name__ == "__main__":
    #  print(findFrequentWordsWithMismatches('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1))

    file = 'Textbook/Chapter1/data/rosalind_ba1i_test4.txt'
    with open(file, 'r') as f:
        text = f.readline().strip()
        k, d = f.readline().strip().split(' ')
        print(findFrequentWordsWithMismatches(text, int(k), int(d)))


