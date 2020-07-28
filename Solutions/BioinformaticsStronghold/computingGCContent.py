#!/usr/bin/python

names = []
sequences = []

def read_fasta(filename):
    f = open(filename, "r")
    seq = ''
    for line in f:
        if line.startswith('>'):
            names.append(line.strip())
            if len(seq) != 0 :
                sequences.append(seq)
            seq = ''
        else:
            seq += line.strip()
    sequences.append(seq)

def get_longest_gc_content():
    max_perc = 0
    pos_longest_gc = -1
    for i, seq in enumerate(sequences):
        gc_perc = get_gc_content(seq)
        print(gc_perc)
        if gc_perc > max_perc:
            max_perc = gc_perc
            pos_longest_gc = i
    return names[pos_longest_gc], max_perc

def get_gc_content(seq):
    count = 0
    for nucleotide in seq:
        if(nucleotide == 'C' or nucleotide == 'G'):
            count += 1
    return round(count / len(seq) * 100, 7)

if __name__ == "__main__":
    filename = '../../Files/rosalind_gc.txt'
    #  filename = '../../Files/fasta_example.txt'
    read_fasta(filename)
    #  print(sequences)
    #  print(names)
    seq_name, max_perc = get_longest_gc_content()
    print(seq_name)
    print(max_perc)





        
