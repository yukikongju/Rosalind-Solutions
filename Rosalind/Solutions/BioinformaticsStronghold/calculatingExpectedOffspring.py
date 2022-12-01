#!/usr/bin/python

""" Link: http://rosalind.info/problems/iev/"""

""" AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa """

GENOTYPE_PAIRING_PERC = [1, 1, 1, 0.75, 0.5, 0]


def getOffspringWithDominantPhenotype(pairings):
    offsprings_per_couple = 2
    total = 0
    for i, _ in enumerate(pairings):
        total += GENOTYPE_PAIRING_PERC[i] * int(pairings[i])
    return offsprings_per_couple * total

if __name__ == "__main__":
    string = '17617 16938 17255 18524 17473 16275'
    num_offspring_with_dominant_phenotype\
    = getOffspringWithDominantPhenotype(string.split(' '))
    print(num_offspring_with_dominant_phenotype)

    
