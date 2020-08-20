#!/usr/bin/python

from scipy.special import binom

def mendels_second_law(k, N):
    def probability(k, n):
        return binom(2**k, n) * 0.25**n * 0.75**(2**k- n)
    return 1 - sum(probability(k, n) for n in range(N))

def read_fasta(filename):
    f = open(filename, 'r')
    line = f.read()
    numbers = line.split(' ')
    k = int(numbers[0])
    N = int(numbers [1])
    return k, N




if __name__ == "__main__":
    filename = '../../Files/rosalind_lia.txt'
    k, N = read_fasta(filename)
    p = round(mendels_second_law(k, N), 3)
    print(p)
