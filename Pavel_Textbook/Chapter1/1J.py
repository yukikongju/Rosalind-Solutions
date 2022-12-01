#!/usr/bin/env python

#  https://rosalind.info/problems/ba1j/
# PROBLEM


#  def findFrequentWordsWithMismatchesAndReverseComplements(text, k, d):
#      """ 
#      Given: A DNA string Text as well as integers k and d.
#      Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern_rc) over all possible k-mers.
#      """
#      # 1. count words mismatches for all kmers and their revers complement
#      kmers_counts = {}
#      rc_mappings = {}        # (substring: rc)
#      for i in range(len(text) - k + 1):
#          # get substring and its reverse complement
#          substring = text[i:i+k]
#          rc_substring = getReverseComplement(substring)

#          # add rc mappings
#          rc_mappings[substring] = rc_substring

#          # add word mismatch count for substring and its rc
#          if substring not in kmers_counts:
#              count = findFrequentWordsWithMismatches(substring, k, d)
#              kmers_counts[substring] = count
#          if rc_substring not in kmers_counts:
#              count = findFrequentWordsWithMismatches(rc_substring, k, d)
#              kmers_counts[rc_substring] = count

#      #  print(kmers_counts)

#      # 2. find the pair (substring, rc) whose count is maximal
#      patterns = []
#      best_count = 0
#      for substring, rc in rc_mappings.items():
#          #  count = int(kmers_counts.get(substring)) + int(kmers_counts.get(rc))
#          count = kmers_counts.get(substring) + kmers_counts.get(rc)
#          print(count)
#          #  if count == best_count:
#          #      patterns.append(substring, rc)
#          #  elif count > best_count:
#          #      best_count = count
#          #      patterns = [substring, rc]

#      return patterns


#  def findFrequentWordsWithMismatches(text, k, d):
#      """ 
#      Given: A string Text as well as integers k and d.
#      Return: count k-mers with up to d mismatches in Text.
#      """
#      # 1. count approximate pattern count for all kmer in text
#      kmers = {}
#      for i in range(len(text) - k + 1):
#          substring = text[i:i+k]
#          if substring not in kmers:
#              count = countApproximatePatternMatchingInString(substring, text, d)
#              kmers[substring] = count

#      # 2. find max_count
#      max_count = max(kmers.values())

#      # 3. find all kmers with max count
#      count = 0
#      for kmer, count in kmers.items():
#          if count == max_count:
#              count +=1

#      return count

    
#  def countApproximatePatternMatchingInString(pattern, dna, d):
#      """ 
#      Given: Strings Pattern and Text along with an integer d.
#      Return: Count number of substring of Text with at most d mismatches.
#      """
#      count = 0
#      for i in range(len(dna) - len(pattern) + 1):
#          substring = dna[i: i + len(pattern)]
#          dist = hammingDistance(substring, pattern)
#          if dist <= d:
#              count += 1
#      return count

#  def hammingDistance(dna1, dna2):
#      return sum(1 for i, j in zip(dna1, dna2) if i != j)

#  def getReverseComplement(text):
#      complements = {'A': 'T', 'T':'A', 'C':'G', 'G':'C'}
#      rc_text = []
#      for nuc in reversed(text):
#          rc_text.append(complements.get(nuc))

#      return ''.join(rc_text)
    


#  if __name__ == "__main__":
#      text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
#      k, d = 4, 1
#      print(findFrequentWordsWithMismatchesAndReverseComplements(text, k, d))


