#!/usr/bin/python

def get_substrings_indexes_with_at_most_d_mismatches(genome, patterns, d):
    """ genome: string ; patterns: substrings ; d: num mismatches"""
    indexes = []
    i = 0
    end = len(patterns)
    #  end = 4
    while i < len(genome) - end:
        #  for j, pattern in enumerate(patterns):
            #  pattern_length = len(patterns[j])
        if hamming_dist(genome[i: i + end], pattern) <= d:
                #  print(i, genome[i: i + pattern_length], pattern)
            indexes.append(i)
        i += 1
    return indexes

def hamming_dist(substring, pattern):
    count = 0
    for i, nuc in enumerate(substring):
        if nuc != pattern[i]:
            count += 1
    return count

def get_patterns_from_string(string):
    return string.split(' ')

def print_list(indexes):
    for index in indexes:
        print(index, end = ' ')
    return

if __name__ == "__main__":
    genome  = 'ACATGCTACTTT'
    string_pattern = 'ATT GCC GCTA TATT'
    patterns = get_patterns_from_string(string_pattern)
    d = 1
    indexes = get_substrings_indexes_with_at_most_d_mismatches(genome,
            patterns, d)
    print_list(indexes)

