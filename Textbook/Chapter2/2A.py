#!/usr/bin/env python

#  https://rosalind.info/problems/ba2a/



#  MOTIFENUMERATION(Dna, k, d)
#      Patterns ← an empty set
#      for each k-mer Pattern in Dna
#          for each k-mer Pattern’ differing from Pattern by at most d
#            mismatches
#              if Pattern' appears in each string from Dna with at most d
#              mismatches
#                  add Pattern' to Patterns
#      remove duplicates from Patterns
#      return Patterns



def motifEnumerations(DNAs, k, d):
    patterns = []

    # 1. find all kmers patterns in list of DNAs

    

def findAllKmersInDNAs(DNAs, k):
    """ 
    Find all kmers of length k in list of DNA strings
    param: 
        - DNAs: list of DNAs strings
        - k: length of kmer
    Implementations:
        - Opt 1: sliding windows in all string and check if patterns is in 
          pattern list (num strings * (len DNA - k + 1) * n)
        - Opt 2: generate all kmers strings
    """
    pass
        




if __name__ == "__main__":
    DNAs = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
    print(motifEnumerations(DNAs, 3, 1))



