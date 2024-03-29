#!/usr/bin/env python

#  Problem: https://rosalind.info/problems/ba1a/


def count(dna, kmer):
    """ 
    Given: sequence (dna), pattern (kmer)
    Return: number of times pattern occurs in sequence
    """
    count = 0
    for i in range(len(dna) - len(kmer) + 1):
        substring = dna[i:i+len(kmer)]
        if substring == kmer:
            count = count + 1
    return count
    

def main():
    print(count('GCGCG', 'GCG') == 2)
    print(count('ACAACTATGCATACTATCGGGAACTATCCT', 'ACTAT') == 3)
    print(count('TACATTACGCATTACGCCGTATTACGCGGTGATTACGCCATTACGCCACAGATTACGCATTACGCTTAGGAATCGCTGTAATTACGCCAAGCTATTACGCATTACGCGAATTACGCAAGCACCGATTACGCAATTACGCGATTACGCACATTACGCTTATTACGCGTTCAAGATTACGCATTACGCAATTACGCTCTTAATTACGCACATTACGCTTGCCCTTATCATTACGCTTACCAACATATTACGCGATTACGCATTACGCATTACGCATTACGCATTACGCATTACGCAGGATTACGCAACGTATTACGCTAGATTACGCTATTACGCGGATTACGCATTACGCATTACGCATTACGCTTGGATTACGCGACGTTGTATTACGCTATTACGCATTACGCATTACGCGAATTACGCAATTACGCCCTCAATTACGCATTACGCGAGGATTACGCCCTATTACGCCTGTATTACGCATTACGCAAATTACGCATTACGCCATTACGCCAAATTACGCTATTACGCATTACGCATTACGCGTATTTAGAGGGTCGATTACGCAGATTACGCATTACGCTGCTTATTACGCATTACGCGGATTACGCCATTACGCACATTACGCGGATTACGCAATATTACGCCTGCATTACGCCATTACGCATCCTTAATTACGCATTACGCATAGATATTACGCATTACGCTAGAAATTACGCATTACGCAATTACGCAGAAATTACGCATTACGCCCTAATTACGCCTAGGTATTACGCCTAGTAATTACGCATTACGCGAGGGGATTACGCTATTACGCCCCGGGGATTACGCATTACGCCATTACGCATTGTTGGGCATTACGCATTACGCAATTACGCCATTACGCGGGTGGTCTCGGATTACGCGGAATTACGCATTACGCATTACGCAATTACGCGATTACGCAGATTACGCATTACGCCGTACCGATTACGCAGATTACGCTCCATTACGCCTATTACGCGGGCATTACGCCACGATTACGCGTTCTGGAATTACGCACTGATTACGC', 'ATTACGCAT'))

if __name__ == "__main__":
    main()



