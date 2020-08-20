#!/usr/bin/python

""" Link: http://rosalind.info/problems/splc/"""

def getProtein(string):
    pass

def readFastaFile(filename):
    pass

def removeIntrons(string, introns):
    pass

def concatenateExons(string, exons):
    pass

if __name__ == "__main__":
    filename = ''
    string, introns, exons = readFastaFile(filename)
    new_string = removeIntrons(string, introns)
    new_string = concatenateExons(new_string, exons)
    protein = getProtein(protein)
    print(protein)

