#!/usr/bin/python

def generate_kmer(genome, n):
    compositions = []
    doubled_genome = genome + genome
    length_genome = len(genome)
    for i in range(length_genome):
        compositions.append(doubled_genome[i: i + n])
    return compositions

def print_list(cust_list):
    for item in cust_list:
        print(item)
    return

if __name__ == "__main__":
    genome = 'CAATCCAAC'
    n = 5
    compositions = generate_kmer(genome, n)
    print_list(compositions)


