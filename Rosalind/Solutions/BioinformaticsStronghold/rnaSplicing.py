#!/usr/bin/python

""" Link: http://rosalind.info/problems/splc/"""

"Delete introns, concatenate exons"

string = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
introns = 'ATCGGTCGAA'
exons = 'ATCGGTCGAGCGTGT'

RNA_CODONS = {'UUU': 'F',       'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
              'UUC': 'F',       'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
              'UUA': 'L',       'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
              'UUG': 'L',       'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
              'UCU': 'S',       'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
              'UCC': 'S',       'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
              'UCA': 'S',       'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
              'UCG': 'S',       'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
              'UAU': 'Y',       'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
              'UAC': 'Y',       'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
              'UAA': '',        'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
              'UAG': '',        'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
              'UGU': 'C',       'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
              'UGC': 'C',       'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
              'UGA': '',        'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
              'UGG': 'W',       'CGG': 'R',      'AGG': 'R',      'GGG': 'G'}

def translate_rna_to_protein(rna):
    codons = []
    for i in range(0, len(rna), 3):
        codons.append(rna[i:i+3])
    protein = ''.join([RNA_CODONS[codon] for codon in codons])
    return protein

def transcribe_dna_to_rna(dna):
    return dna.replace('T', 'U')

def readFastaFile(filename):
    pass

def removeIntrons(string, introns):
    return string.replace(introns, '')

def concatenateExons(string, exons):
    return string + exons

if __name__ == "__main__":
    filename = ''
    #  string, introns, exons = readFastaFile(filename)
    string_without_introns = removeIntrons(string, introns)
    #  print(string_without_introns)
    #  concatenated_exons = concatenateExons(string_without_introns, exons)
    #  print(concatenated_exons)
    #  rna = transcribe_dna_to_rna(concatenated_exons)
    rna = transcribe_dna_to_rna(string_without_introns)
    protein = translate_rna_to_protein(rna)
    print(protein)
    

