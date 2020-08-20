#!/usr/bin/python

def read_fasta(filename):
    f = open(filename, "r")
    sequences = []
    seq = ''
    for line in f:
        if line.startswith('>'):
            if len(seq) != 0:
                sequences.append(seq)
            seq = ''
        else: 
            seq += line.strip()
    sequences.append(seq)
    return sequences

def get_profile(dna_strings):
    length = len(dna_strings[0])
    profile = []
    for pos in range(length):
        line  = [0, 0, 0, 0] # A,C,G,T
        for dna in dna_strings:
            if dna[pos] == 'A':
                line[0] += 1
            elif dna[pos] == 'C':
                line[1] += 1
            elif dna[pos] == 'G':
                line[2] += 1
            elif dna[pos] == 'T':
                line[3] += 1
        profile.append(line)
    return profile

def get_concensus(profile):
    """ two for loops and keep track of pos max nucleotides within a line"""
    DICT_NUCLEOTIDES = ['A', 'C', 'G', 'T']
    nucleotide = ''
    for i, _ in enumerate(profile):
        pos_max_nucleotide = 0
        max_nuc = 0
        for j, _ in enumerate(profile[i]):
            if profile[i][j] > max_nuc:
                max_nuc = profile[i][j]
                pos_max_nucleotide = j
        nucleotide += DICT_NUCLEOTIDES[pos_max_nucleotide]
    return nucleotide

def print_profile(profile):
    nucleotides = ['A', 'C', 'G', 'T']
    string_length = len(profile[0])
    for i, _ in enumerate(nucleotides):
        print(nucleotides[i], end = ': ')
        for j, string in enumerate(profile):
            print(string[i], end = ' ')
        print()
    return

if __name__ == "__main__":
    #  filename = '../../Files/concensus_and_profile_example.txt'
    filename = '../../Files/rosalind_cons.txt'
    dna_strings = read_fasta(filename)
    profile = get_profile(dna_strings)
    concensus = get_concensus(profile)
    #  print(dna_strings)
    #  print(len(dna_strings))
    #  print(len(dna_strings[0]))
    #  print(profile)
    print(concensus)
    print_profile(profile)

