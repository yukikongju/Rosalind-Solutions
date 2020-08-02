#!/usr/bin/python

def count_substrings(genome, n):
    substrings = {}
    i = 0
    while i < len(genome) - n:
        if genome[i : i + n] not in substrings:
            substrings[genome[i : i + n]] = 0
        else:
            substrings[genome[i : i + n]] += 1
        i += 1
    return substrings

def get_most_frequent_substrings_from_dict(substrings):
    max_value = max(substrings.values())
    max_keys = [k for k, v in substrings.items() if v == max_value]
    # print(max_keys.sort())
    return sorted(max_keys, reverse = False)

def print_list(most_frequent_substrings):
    for substring in most_frequent_substrings:
        print(substring, end = ' ')

if __name__ == "__main__":
    genome = 'TGTGGGATGTGGGAATCTGGGGGCCCGGGATCTGGGGTGTGGGAATCTGGGGTGTGGGATGTGGGATGTGGGAATCTGGGGTGTGGGAGCCCGGGCTTGTACTGTGGGACTTGTACCTTGTACCTTGTACCTTGTACTGTGGGAAGATATGCGCCCGGGAGATATGCGCCCGGGGCCCGGGAGATATGCCTTGTACGCCCGGGCTTGTACAGATATGCTGTGGGATGTGGGACTTGTACAGATATGCGCCCGGGGCCCGGGATCTGGGGATCTGGGGAGATATGCATCTGGGGCTTGTACGCCCGGGTGTGGGACTTGTACATCTGGGGGCCCGGGAGATATGCTGTGGGAAGATATGCCTTGTACAGATATGCATCTGGGGCTTGTACAGATATGCTGTGGGAGCCCGGGGCCCGGGATCTGGGGCTTGTACATCTGGGGATCTGGGGCTTGTACCTTGTACTGTGGGACTTGTACAGATATGCGCCCGGGAGATATGCCTTGTACTGTGGGAGCCCGGGTGTGGGAGCCCGGGCTTGTACGCCCGGGGCCCGGGAGATATGCATCTGGGGTGTGGGACTTGTACCTTGTACATCTGGGGAGATATGCATCTGGGGTGTGGGATGTGGGAATCTGGGGCTTGTACCTTGTACTGTGGGACTTGTACGCCCGGGCTTGTACTGTGGGATGTGGGATGTGGGAGCCCGGGAGATATGCGCCCGGGTGTGGGAATCTGGGGATCTGGGGCTTGTACAGATATGCCTTGTACGCCCGGGGCCCGGGTGTGGGATGTGGGAATCTGGGGAGATATGCTGTGGGA'
    n = 13
    substrings_count = count_substrings(genome, n)
    most_frequent_substrings = get_most_frequent_substrings_from_dict(substrings_count)
    # print(most_frequent_substrings)
    # print(most_frequent_substrings.sort())
    
    print_list(most_frequent_substrings)


