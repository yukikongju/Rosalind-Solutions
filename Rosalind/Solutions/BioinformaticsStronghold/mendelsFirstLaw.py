#!/usr/bin/python

""" Link: http://rosalind.info/problems/iprb/"""

""" Help: https://www.thagomizer.com/blog/2014/11/19/approaching-rosalind-problems.html"""

""" Dominant Allelles: Aa or AA """

def getProbabilityDominant(homozygous, heterozygous, recessive):
    total_population = homozygous + heterozygous + recessive
    recessive_recessive = (recessive / total_population) * ((recessive - 1)
            / (total_population - 1))
    hetero_hetero = (heterozygous / total_population) * ((heterozygous - 1)
            / (total_population - 1))
    hetero_recessive = (heterozygous / total_population) * (recessive
            / (total_population - 1)) +\
            (recessive / total_population) * (heterozygous / (total_population - 1))
    recessive_perc =  recessive_recessive + hetero_hetero * 1/4 + hetero_recessive * 1/2
    return round(1 - recessive_perc, 5) 

if __name__ == "__main__":
    k = 28         # num homozygous dominant
    m = 23         # num heterozygous
    n = 19         # num homozygous recessive
    probability = getProbabilityDominant(k, m, n)
    print(probability)

