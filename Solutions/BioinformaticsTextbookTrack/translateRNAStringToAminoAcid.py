#!/usr/bin/python

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

def translateRNAToAminoAcid(genome):
    amino_acid = ''
    for i in range(0, len(genome), 3):
        amino_acid += RNA_CODONS[genome[i: i + 3]]
    return amino_acid

def read_genome(filename):
    genome = ''
    f = open(filename, 'r')
    for line in f:
        genome += line
    return genome

if __name__ == "__main__":
    filename = '../../Files/genome_example.txt'
    #  filename = '../../Files/rosalind_ba4a.txt'
    genome = 'AUGACCGCGACUAGGGCCCUCGAAAGCCACGUACUCAAGAAAAACAGUCCAGUCCUCGCCUGGGGAGGACUGCCGGGACUCUCGCCACUAAUGUGGAGUCUUUACCCGUCCGUGAGUCACGGUCGAUCAGCAGCCGGGAAAACCCAUCUGGGACCAUUACAUCGCGGAGCUGUCAUCGUCAAUCUUGUUGGAACGGUCAGUCCGAGUUCUCAUGUUCUAAGUCAGCCGGUAUAUGUCAAUGUAAGCGGCUCUGGGGCAGUACUUUGUUAUCUAGAGUACCCGAAUGGUGGAACCAGGGGUCCGAUAGGCCCCUCGAAAGUGCGAACCGAUCCUAGCUUCGUUGAAAGUUCUAGGGGUGAUGUUAUAUGGAUAUCGAUCGGGAUGCCUGUAUCUCGGGCCACAGCGGUUACACUUAGUCUCCCGCACAGUGACCAAAUGAUACCUAGUCUGCGCCAUGCAACAUAUUGGAGGGGAUACCAGACCGUAAUCGCCCGGGCACGGCCACGUAAGUAUGUCCACCGAAAAGCAUUCGCAUCGCCGAUACAGGUCUUCUCGCGGCGGUGUACUUCUAAGAUCCCACAUAUGCUUGUGACUAUGAUUAAACCCAAAACACUGCCACGGAGCGCAUGGGUCGCGGGCAUUGAGAACAACCCCUUUCCAUCAGGUCAUCUCGUGUAUACAUACACCAGGGGUGCCGGCGCGCCUCCGAAGUUUAGUGCCAAGCUCUUUACCGUAAACGACGUCGGGAGCUUAUCUUAUUGGUACAUUACCUACUUGCUUAAGCUGACACACAAUACCAGUCGAUCCUGGAGCUGCGGUAUAUCUAGGGUUGUGCAAAGCUUUUUCUUGAACCGAUUGCGGAAAAAAGCCACGAGUAAGGCAGCUAGAACGGUAAAUCUCCCCCUCCAGUACGUAAUCGACAUAUGCAUGACGACGUGUUCGGGCGAUUGUGCCCAAUUCAACUCCUUAUUCUUGGUGAUGUGGAUCCAUUGGGGAGCCCUAUGUGGGACACCAUGCGGCCGAAAUGUUCGCUACAGCCUUAGCCUUGCCUCAAUGGCGCACGUCAGACCCACUGUCGGCACGCGCUACCUCUACCUGAUAGCACAAAAAAACUUUAACGAGAAAAUUCAGAACCGGGACAACUUUGUGCCGAUCUCACGAUUACGUCAAGACCCGGUCGCUUCCAGUCCCUUUAUGAAAUUGGCCAAAAAGCGGUCGUCAGCAAUUGCACACCAACUCGAAGCCGUAGAAAAGCUUGCGCGCACUGGGGCAAUGCGCCAGGAUACCAAAAGUGCGCUAGAGUUGACAACUCGAAUUGGUCAUCACAAGUACUGCGAGGAUUGUUCAAAGGCGGGAGUUUGGGGCGCAGUAGGGGAUCACAAACAGCUGGUGAUCACUCGUCCGGCUCAGCAGCCUGCUUAUUAUUACUUACGGUCCGGUGUCGAGUCUAUCGACCGAUCGGUUGGCUCGUCGAAUCAAAUGGGACAAUCGCUAGUUGCUAAACCGUCAGACGCAUUUCCGAGCCCCCCGUUCACUCCGACUAAUAAUAGCUCAAUGAGAAAAUUGUGGGAGCGCCAACGCACCACCUUACACAUGUCAAACUCACACUGGCGCGUUCCCUCUUACGCUAUGUUAGAUGGCCUUAAUCGCUCUGGUGCAUGUUACUCAACUGGGCAUCGGGCACCAGUAAUGGCUCGUAGAAUCCCUGGGUCUAGAUACACGCAGUGUUUAUUACCCCCAGCAGUUAAGCACCUCACGUCGAGUUUACGACGACUAAAACCCGGUAUGAAGUGUGUGAUAAUGUGCCCGUUUAACCUUGUCCUAGCUCAGGGCGGUCGACUCCUAGCGUACCCCCACGGACCUGCCUUGCGCAGGGUACAAACUUUGAGAGGGCAAAGUGCCGCUUCGACCCUCAGAGACUUCCACAGAAUACUCUACGCUAUAAGUAGUGGCCUAUGGCCCGUACAUAAUAUUUCAAGUGUACGGCGCUCUGAUCUACAAGAGGCCACUAACCGGACCGAAUUUGCCUCCGCUUGCUGCGACCUGUGCCCCCCCCUACGCCGCCUAGAGGCCUCGGUGGCGAUUUUUAGAUACGGCCCCAUUCGACAAGUUGUAACACUUCUCUCAAAUGUAAAUAGGGACUUCAGUAAGCUACCGAGCCACGAGCCACUUGAGAACGGUAAUAUCAUGUUGCUGAAUUAUGGCGGGAUCAGCGGUAUACAAAUGUAUACUAGCUUCCAGUUCUCGGGGGGUCGGACACCUUACUCCCCUAAUGGACGAACCGCUGUAAUGUUGUGCAAGGGCCGCUACCCAUCGGUCAAUGGCUGGCCGUUGCAGAGCACGCCAUGGCAUCUCUUGCGCAAGAGUAGACUCGGUGCGCUAAUAGCGCAAGAUCAACUGAUCCGCGAGGAAGUGGCAUCGCUCAGAUGUAAGCGCGGAUUUUUGUUCCGUGGAGGCCCACGCGCAUCAUCCAAUCGCUUCGGUACCUCAUUCUGGCUCCCUAAUCCAGACAGAGUUCAUUCUUUUUGUAAUCCCCGAUUGAUAGUCUUUUGUUUGGGCCCAGCUGCUCAUGGGAUUUCACGUAUAAUGCAUACUAAUGUUCUAUUGAUUAGAAUUUUCAAUGACGCGACUUUUCCCGUUUGGUACGUCCCUCCACGCCCACCCAUGCACCACAUCUUUUGCAACGGUCGUUUCAACCAUGGUAGUGCUCCUCUGAGGUGCGAUGAUCACUGUACUGUCAGCGUGGCCGAUGAUAGGACAGUCACGAGAAGGCGGACCUGGGGGCACAUUGCCGUGGAGGCUGAAAUAACACUUUGGGCUGACGAAGUUACCAGCCACGGAAUUCUGGUUCCCGUGUAUAUCGCAUCGACGUGCUCCUUCUGCGUGGGUUUUCAGCGCCUUGUGGAAACAUAUACCCUAACCACUGCGUUGCGUGGCCUCUCUGCGAGGGGAGAGGGAAGGCCUCUGACUGGCUCUGUUUAUUUUACUAUGCAGAAGACAGGAAACUCUUGUGAGUCUACGCGUAAUGCGCCUUACGCUCGGGAGGGCCGCCUUAACGUAAUAGUAAAAUCAUGGCCAUGCCGCGACAUAAGUCAGUAUGGAGACCUGUGUCCUGCCCAAAAUCUAGUGCGCCUAGUUAAUAGUCCGAUCCGAAAUCGUAUUACCCGACUGUGCGUGAUGUGGUGCGUAACCCUCUCUACAUUUUACUACGGAGAGCAGGGCCCUCAUUCUCACGCAAUACACUAUUGCAAACACUCCGGAUUCACGUGCCGUGCAUGCAGCGAAACCGUCAAAAUCUUACGUCUAGGGGCAGACGAACAAUGUAGCACGGGCCGUGUCUUAUUAGAAUUGAUUUACCCUAUUGGGAUCAGACGCACUGCUACCUCGCCCUUUGGGCGAUUGGUGAACAAUACUUGGUCUUACAAGGGAUCUAGGGGUUCGGCACCGUACAGAGACGAAUAUAGCCCGCUGCCUUGUGCGCCCAUUAAUCGAAACGCCACGAGGGGAGCCAGAGGCUGCGCUUUCCGUACCACUUACGUCUAUCAGCAAAGGCUCCUUCGUUCGCCAAGGGCCGGGAUGAUGCCUCGAACGAUACCUUUUUGUAUAUACGGCCAUACGAGCCUAUUUGACCAAAACGAGAUAAUACAAGGUAGAGAUUAUCGACGGUAUGAUGUGUUUCUGGAUGUCCGGAUGGCAUGCUCGCUCAGAGCAGCAGUGCCGAAGUGCCGUCCUGAUCCUUAUAUUAAUCUUAUAAACGACCUAGUUUGGGUUAUUGAGGUAGCCUGCACUAAUCAGUGCCGUUUCGGAAUCCCGUCCCCCCUACAGACUAUGAGUAUCCUAGCGCCGAAUCGAAGGUGUUUUUUUGGUAAAACUAGUUGGAGUGCCGCCCUACUCCAGUCUGAUUUAUCAGAUACGGAUCUGCUAGGUUCCACUUGUGCGUCUUGCCAGUGGCUACUCAUCAACGUGAUGAGGUCAGGAUCAGCCGCGUACGGGAGAAUCCACCCCACAGGCCCUAGGUACUAUGCAUUACGAUGCAUGAACAAUGUUAGACUUACGGGUACGCCGAAUGCAAGCCGAGCGGGAAAUAAAUUGCACCCCAGGCCAGAAACUCCCGAGGGAGCAUCCGCAAACACCCAUGUACUGAUAGAGCCAAGGGGCGUGGUAGUGUCGUGCGAUUCUCGAUCUAAUGCAGGAGUACAGAGGCCGAAUCCGUCCUCGAAUAGGCGCGAUUGUCCCGACACUUCCAACGCACAAGUAGCUUACAGCCAGUUACCAAUACCGACUACGGUACUAGACCCGCACAACAGAUACCCUACGGAUGCGACGAUGAAAGGUACCCUGGCCUCGCAGGAGUGGGCGCCUGACAUAGACCUCAGCACGGUGGAACCUCGGCGCUUAAUUUUUGAAGGGCAAAACCGAAAGAGAGACCCCGCCGACCAUUAUAACUAUUGGAUUAAUUUGAAGGGUCCUGCCCGUGAUAUAUUGAUAGAACAACGCUACUGUCUCACAGACAGCCCUCCGCGGAGAGAUAUGUGGUUCUGUACAGAGGCAUUAUGUCCACGGGCUAAUUGCUUACAAGCAAUCCCGAGACUGUUAGGGCCUUGGCAUUAUACUUCACGUGACCGACCUUACACCAUUUACGUCCUACGGCCACUGUUCAAGUAUACCAGACUUGUGCAUUCGAUCCCGAGUUCGGAAAUUUUUUUUCCAAUUGAAGUGAGGGUCCCGUUAUUCGAAAGCCAGGGUAUAUACACCGUGAAUUUCUUUUCUGACUCACGGUGGGAGGCUGGACUCCAGGAGCAAUUGAUCAAUGCAUGUCGUGGAACAUGCUCUAUCACGGGUCUGCUAAUGGAGGACGCUAGCAGGCCCCACAACCUUGAAAAAGAACCCGGUGCAAUACUACGUGUCAAUACGAUGGCGACCCUCUACCGACCGCUAGGGACUGACCUCCUUCCAAAGAUCCUAGUUGAGCUGCACGCGCCGGAGCUCGCUCGCAGUGUUCUUGGCGAACUGUGCAUUGGGAGGAGUCGACGACCCACGAAAUUUUAUCACACAGCUGGGCUGUCGCUAUCUCGUUUUUCUUUCCGACCCGUGUGUGCUGCCGAGCUGGAACGUCGCGGGAUAGGCGCAGCCCGGACUCGGGUGGACCACAAGGCUAUACACUUUUCGGAAGCCCGGUAUAGCGCAGGUCACGUGCAAACAAUUAAUGAAAGACAGUCGAAGGAUAAGAGCUGUGUCACACCUGUAAUCGUUGAACUGGUCGAUGCCUGGGAGCAUAGUAUUAAACCCCCCUACCGUCGCGCAUUCCUCACACCGAUACCUAGGGUGCGACUUUUCUCAAAACCAAGAAGAACUUCCCCAACGCUUUUUUACGGUACGCACCCGAGUAGCGUUGAUUUCCGAUACUUUAGUUACCCUGCCCCACCACGAGGAGGGUGGAUUUAUAGCGAGAACAACUGCCCGCUUAAGAUGAACUUACAGAAAAGUCCCGAGCUUUAUAGCCUAAAGAAGCCCGGAGAUCCUGUCCUGGGCCCGCGAUGCGACCAUUGCCUACAGGUGACGCGCAGUAUUCGUGGACGGCCGGACUAUGAAGGCGUUGAUACUGACAUCUUUAUGUUGACUUCACAGGGCUGUCAGGGUCUAUCCCUCAAUGACCCUGGGUAUUUCUGUGUGCACUGCUCGUUUGAUUCGCACUCCCUUCAAGGAGACCGCUUCUUGAUUCUGCGCGAGCUGUUGGAUGCCUCUUACCUGGGGUGGCGAACCCACUACAAUCGAUCUCCAGCCUUGUCCUACCGGUCGAUCGUGCAUGAUAAGGGCAGGAAGACCCCUGCCAAAUUUUCCUGGUAUAGACCUGCUCGGCAACGGGGGCCGUGUGUAGUAAUGUACUCAGUUACCGGUUGGUUGCCCAGACGAUCCAAGGUCACCUCAGAUGCCGGGCAUCAAAUCAUGGUCACAAAAUUGCGAGGGUCAACCAUGUCCGCAAAUAGUCAGUGCGUCAUUCUCGUUGUGCUUUCUAGAAGGGCAGAAAAGGAAUCACCCUUAUGCGAAACUGCCCGGGCUUUGGACGAAGCUCGGAACCCUCGGAGUUGGGAUGGAGUUGGUCGGGUUAGGACGCAGAGUAAUAACGCGUACGUCGUUAAGUCAUACCGGAUAGAUCGUAUUACUCAGAAGGGCCCGGGACAAAGGGAAUACACUUAUAUCUACUCAACUAAUCAGGACUCAGCUUUGCUUUCCGUCAGAAAAGACCCGCUACACAUAGCAAUCUACUUCACGUCCCUGUGCCUCAUCUCUAACUUGACAUGCCUGGAGAUGCCCUUAAAGUUCGCCGUUCAAUCCCGAUGCGCCUUCUCCGUGUACCUCAAUGGUGACAACGUGCAAUCACCAGUAAGUCUAUUGUUGCACAAGUAUGGGCCAUAUUCCCCUGUAAGUCAGAAUAAUAGGAGGAACGGACUAGCUGCCACAUUGUACUCGAUCCCGCUGAGGUCGGUGUCCAAGUCAGCUUGGUUAAAUAGCCAAUGUAUCGAUACAAAACCUUCACCUAGCGCGCACCUCCCAAACGAUGUUCCGUGCUGCCAUAGUUCGGUGUGGGACGUCUCAUUACGAGUGAGGCCUCGGUCACCAGGUCAUAUAGAGAGUGAAGGCACUCAGUUAAUCAGAGCCGUGCGGGCUCCCAGCUAUGGUAGCCGAUCUACCGAAGAUAGCCUCUCGAAGUUUUAUUUGAUAGAAGCUACUGACCCCUCCGUAAUCUGCGGAAUCAGUUUUCUGCAUUCGGAUAGGAGUGAUGUGUUACUGAUGCACGGGGGGGUACUCCGAAGCAGACUUGGUCAUAAGGCCUCGGUUAGCAUAUAUGUCAAUCUCUCUAAAAGGUCACCCUUAGUAGACUUCUUCCGCCAGUCGGUAAUCGAAUUCCAGUUCGUUCCCGGUUCAUCGCACCACGGUAGGCCGGCCAUGUUAAUUGAGCCGGGAUCGGGGGGCGAGCUCAACACAUUUGUAUGGUCGAACCGCGGCUUCCGUUACGUCUGUUAUGUGCGCGUGCCAAUAGCUCAGCUAAGCUUCAAAGUACCCACCACGACCCAUACUAUGCGCCCUUUGUUUCGCUAUCCGGCCCAUGCUACUCCCUCGGUGGAUAUGAUCAGACUCACCGUAUUAGGCGCUUAUGUUCAGAGGAGAGACGACUUUUACAUACGGAUUAAAGGCUAUCGCUCUGCGGGUGUCUCCAACGGGCCAGUUUCCCAUUGUUCGUGUGAACCAGGAGGCACUAGCCUUAUGAUACGGAUAGCCAAGACGCUAAGCGGGCAGCCCUGUUGCCACGCAAUUUGGCUGUCCCUUGGACUCAACCAGCAGGCCCGUUCGUUUUGCGAGCGAUCGCCCUCCAGUGAUCCACAUGCUCGAAGCUGCUCGACUUGUCGUCUGCCUACAACACCAUGCAGACGUAGACGUCGGCGGAGAGUGUCCGUACAACGUACGGUUGACUCGCCUGGCGCGCUAGAGGCUAUAGGCUUUCCUUUAAAUGUUCUAGGCGCAGCGCCGUAUGCCUGUUAUGAUUUUCCACUAAAUGAGGGGGACCCUUCGCUAUGUAUUGUUUCACUACCAAGGACCCCGAGUGAUAUCGAAGGCCCGCAGCUCCAAUGCACUUACGCGCCCCGUCAUCAGGCUUCCUACAACUCUGACUCCGAUAGACUUUGCGCUCUGUACACUUAUAGUGGUCUUUAUGUGACUGGAACCAUCACCGCCCGCGGAAUGAAAACUUAUAGCCCCACUGACCUUGCUAUCUAUGAGUUUAGAUUUUAUUGGGCGUCUUCCUCCAUAGCGGUGGCACACCACGAUGGUUCAGGCACACUGUCAUUGCGAGUGAAAUUAGCCUUGUGUUUUCCCGCGGUCCUAGGCGCACUAAGUAGAGGUACGCGAAAUUUACAGACUAAGCCAAUAUUUUGCCACACCUCGUCUUGGGGACACCCAGGUGGUCACCAUAUCCACCUGCGCGCUUCGCUGCUGGGUUUGUCCUAUCUCCUAACUCCAAGCUGGCGUACUGCUGUAUACUUCAGUCAACCCGCUUGCAGAAGUGCAUUUCGCUGGCAAAGAAGGUCAGCCAGGCUCACUAAAAUCAACACUACUUUCUCUUCCCGAGGCCUGCGUAGGCUUCCCUCAUGCGAUAGAUAUACGAUGAAGACAAAGAUAGCUUUUCCGUUCGAAGGUGCGUUAAGUUUGUUAGACUUACCAAAGUAUGGUGACCCGCUGCUCUCCUUUGGAGUAACUCUUCGACACCUAUCUCUCCUUUCCUGUAUCAUACAGGAGAAUCCGACCAUUUAUGCGCACCAUUCCGCCCCAAGUAGCACCAAGUUUCCCGACCUUACUAUACGCAAAUACCUAUCAUUUCACUUACGAAGUCGUCCAUGCGGGGGUCUGUUUUGCCGACUAGUUACAGUUCACUUCUACUCUCAUAGCGUUGGUUUCGCACACGUCGUGAGGGUGACAAGAUUGUCUCAAGCAAGGAAUGGUCUACUAGACUCAGCAUCCUCGUUAGGCCUACCGCGAUUCAAGCCACUCACGAUUUCCCAUUCUAAGAGGUUGCACUCCCUGCCACCAAUGAUCACUACGGCUAACCCAAUGAUACGGUGUGAGGAGUGGCCUACGUCUAUUCUGCCGGUCAUCGAUGAAUUCAAUCGACCGGUACUGCUAGAAUUAACCGUGAUUCCGAAGGGUGCGAACUUAAGAUCGUCGAAUUGUGCUCCACGAGUGCUAGGCAACACCGGUGAACGGAAUUUAACGCUACUGGUCGUCCUAUUGCGUGCGACUUCUAGAGAACCGGCGUCUUCGAGAGUGGGAAACACCCGCCCAGCCUUGUUAAGAUCCUUUCCCAGGGCACCAUACGGAAAGACCCUGAAAAGCAUCGGUGGCUCCGGCACUGCAUGCUUGCGACUGGUCACCUUAUAUUUACUCGCAAGGGAACUAAUCCCGCGGACCCCAACGCGCGGACCCGGCUCACUUGCCAACACUCCCUUGUGUUGCAUGCACACUUAUCGUAGCUUUGCUUGCCCUGACCCUGCGCGGGCUGCUUUAACCGGAAGGUCUAGAUCUAGUGAUACUUCGCGCUCAGGAUUUCUUGUGGUCAGAUCAGCACACUUUGAGAGCUGCGGACUGAAGCAGGAGACCUCCUACUCUUUCAUCUGUCGGCUGCGCAUAUGUAAUGUAACGGGCGUCCAGCAUCAAGCGACUUGUGAAGAGUCUAUGAUCGAUUUUGUUAAUACGUAUCAUAUUCGCUCCCAGCUGCAAGUCCCGUCAAGACCCUCAAGGCAUAGAUGGCGAUUUCCUGGUCCCUUGAGCACUGGAUGGAGCUUUAGCAGAUGGGGUUCCGGAGUAGUGACGACAAUUACGUGGGCACUUACUCACGCUCGAGCAUUUCAUGUAUCGCGGGAUAUAUGGGUUACCGAAUUAGCAUGCCUCUUUCCGACUAAUGCCCAGAAGUCACGGAAUGGUCCACCGGUCCGAGGUUCCAGUAUGACCUUAAUAUUCACAGUAACAUUCUGGGGAAUGGCAUGCCGUCUGUUUUUUCGGGUCAGUGCGGGGCGCCAAGGGAUGCAAUGUCUUAGCCCGAUUCCGAACGAAAUGAUAUCACUCCAUUGUAUUCGGUCACCGUUUCAUUGCACUACCGACCAUUCGGUUUACUGUAUUGCGUCUUUCACACACUUGCUGCGCCAUCGGUCUAAGACAAAUUCGGCAGUAAGGUGGUCGCACCUCCGAAAAGGAGGCGCAAGGUUGUUAGAUCGGAUCAGACCACCCCCCUACGCCAUACGAGCCCAAGCUUCGUACCGAAGCGGUAGUUCAAUAUCUAUUCGUCAUGACACGAAGCUUAACGUCCCAUUGUGCUUAGAAUUACAUGCAUGUCCCUUUCAGGUCCCUCCUUUGUCCUGUUCUGAGAACAUUCCGAAUGACACCGUUAAAGUAGAUCCCCAACUGGUGCGACAGGAACCGCUCCGACCAUAUGCCAUUGCAUAG'
    #  genome = read_genome(filename)
    amino_acid = translateRNAToAminoAcid(genome)
    print(amino_acid)

