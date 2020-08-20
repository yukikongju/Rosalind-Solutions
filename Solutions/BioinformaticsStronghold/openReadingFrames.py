#!/usr/bin/python

DNA_CODONS_DICT = { 'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V', 
        'TTC':  'F',      'CTC':  'L',      'ATC': 'I',      'GTC': 'V',
        'TTA':  'L',      'CTA':  'L',      'ATA': 'I',      'GTA': 'V',
        'TTG':  'L',      'CTG':  'L',      'ATG': 'M',      'GTG': 'V',
        'TCT':  'S',      'CCT':  'P',      'ACT': 'T',      'GCT': 'A',
        'TCC':  'S',      'CCC':  'P',      'ACC': 'T',      'GCC': 'A',
        'TCA':  'S',      'CCA':  'P',      'ACA': 'T',      'GCA': 'A',
        'TCG':  'S',      'CCG':  'P',      'ACG': 'T',      'GCG': 'A',
        'TAT':  'Y',      'CAT':  'H',      'AAT': 'N',      'GAT': 'D',
        'TAC':  'Y',      'CAC':  'H',      'AAC': 'N',      'GAC': 'D',
        'TAA': 'Stop',    'CAA':  'Q',      'AAA': 'K',      'GAA': 'E',
        'TAG': 'Stop',    'CAG':  'Q',      'AAG': 'K',      'GAG': 'E',
        'TGT':  'C',      'CGT':  'R',      'AGT': 'S',      'GGT': 'G',
        'TGC':  'C',      'CGC':  'R',      'AGC': 'S',      'GGC': 'G',
        'TGA': 'Stop',    'CGA':  'R',      'AGA': 'R',      'GGA': 'G',
        'TGG': 'W',       'CGG':  'R',      'AGG': 'R',      'GGG': 'G', }

def get_reading_frames(string):
    pass

def translating_codons_to_symbols(dna):
    codons = []
    for i in range(0, len(dna), 3):
        codons.append(dna[i:i+3])
    symbols = ''.join([DNA_CODONS_DICT[codon] for codon in codons])
    return symbols


def read_dna(filename):
    with open(filename) as f:
        next(f)
        dna = ''
        for line in f:
            dna += line
    return dna

def read_dna2(filename):
    f = open(filename, 'r')
    strings = f.readlines()[1:]
    f.close()
    return ''.join(strings)

def print_list(reading_frames):
    for frame in reading_frames:
        print(frame)

def get_reverse_complement(dna):
    COMPLEMENT_DICT = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'C'}
    complement = ''
    for nuc in dna:
        complement += COMPLEMENT_DICT[nuc]
    return complement[::-1]

if __name__ == "__main__":
    filename = '../../Files/open_reading_frames_example.txt'
    dna = read_dna(filename)
    #  print(dna)
    reverse_complement = get_reverse_complement(dna)
    """ Two types of reading framesL: one that come from string itself and one
    from reverse complement """
    frames_from_string = ''
    frames_from_reverse_string = ''
    symbols = translating_codons_to_symbols(reverse_complement)
    print(symbols)
    #  reading_frames = get_reading_frames(dna)
    #  print_list(reading_frames)
