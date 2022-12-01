#!/usr/bin/python

def read_sequences(filename):
    sequences = []
    with open(filename) as f:
        for i, line in enumerate(f):
            if i % 2 != 0: # if line number is odd
                sequences.append(line.strip())
    return sequences

def find_longest_substring(sequences):
    left, right = 0, 0
    longest_seq = ''
    """Sliding window approach and verify if subsequence is in all others
    sequences"""
    while right < len(sequences[0]):
        subseq = sequences[0][left:right]
        contains_subseq = True
        for i in range(1, len(sequences)):
            if subseq in sequences[i]:
                continue
            else: # sequence does not contains subseq
                contains_subseq = False
                break
        
        if contains_subseq is True:
            right += 1 # increment right index if all sequences contains subseq
            if len(subseq) > len(longest_seq): 
                # if subseq len > longest subseq, then update longest subseq
                longest_seq = subseq
        else:
            left += 1
    return longest_seq

if __name__ == "__main__":
    #  filename = '../../Files/finding_shared_motif_example.txt'
    filename = '../../Files/rosalind_lcsm.txt'
    sequences = read_sequences(filename)
    print(sequences)
    longest_substring = find_longest_substring(sequences)
    print(longest_substring)
