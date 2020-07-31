#!/usr/bin/python

def read_file(filename):
    genome_path = []
    f = open(filename, 'r')
    for line in f:
        genome_path.append(line.strip())
    return genome_path

def get_genome(genome_path):
    genome = genome_path[0]
    for i in range(1, len(genome_path)):
        genome += genome_path[i][-1]
        # print(genome)
        # print(genome_path[i][-1])
    return genome

if __name__ == "__main__":
    # filename = '../../Files/genome_path_example.txt'
    filename = '../../Files/rosalind_ba3b.txt'
    genome_path = read_file(filename)
    genome = get_genome(genome_path)
    print(genome)


