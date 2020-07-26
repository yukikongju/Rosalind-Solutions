#!/usr/bin/python

""" Link: http://rosalind.info/problems/iprb/"""

""" Dominant Allelles: Aa or AA """

def getProbabilityDominant(k, m, n):
    total_population = k + m + n
    return 1 - (n / (total_population))

if __name__ == "__main__":
    k = 2         # num homozygous dominant
    m = 2         # num heterozygous
    n = 2         # num homozygous recessive
    probability = getProbabilityDominant(k, m, n)
    print(probability)

