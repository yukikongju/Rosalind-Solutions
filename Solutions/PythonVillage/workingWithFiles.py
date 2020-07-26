#!/usr/bin/python

""" Link: http://rosalind.info/problems/ini5/"""

def readFile(filename):
    lines = []
    f = open(filename, 'r')
    for line in f:
        lines.append(line)  
    return lines
    
def printEvenLines(lines):
    for i in range(1, len(lines), 2):
        print(lines[i])

if __name__ == "__main__":
    filename = 'Files/rosalind_ini5.txt'
    lines = readFile(filename)
    printEvenLines(lines)


