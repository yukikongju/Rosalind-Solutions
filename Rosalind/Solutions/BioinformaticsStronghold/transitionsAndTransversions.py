#!/usr/bin/python

""" Link: http://rosalind.info/problems/tran/"""

""" Transitions: A-G, T-C
    Transversions: A-C, A-T, G-T, C-G"""

NUCLEOTIDE_TYPES = {'A': 'purine', 'G': 'purine',
                    'C': 'pyrimidine', 'T': 'pyrimidine'}

def getTransitionsAndTrandversions(s1, s2):
    pointMutations = {'transitions': 0, 'transversions': 0}
    for i, _ in enumerate(s1):
        if NUCLEOTIDE_TYPES[s1[i]] == NUCLEOTIDE_TYPES[s2[i]] and s1[i] !=\
        s2[i]:
            pointMutations['transitions'] += 1
        elif s1[i] == s2[i]:
            continue
        else: # is a transversion
            pointMutations['transversions'] += 1
    return pointMutations

def getRatioTransitionTransversion(pointMutations):
    return round(pointMutations['transitions']
            / pointMutations['transversions'], 11)

if __name__ == "__main__":
    s1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
    s2 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'
    transitions_transversions = getTransitionsAndTrandversions(s1, s2)
    print(transitions_transversions)
    ratio = getRatioTransitionTransversion(transitions_transversions)
    print(ratio)
