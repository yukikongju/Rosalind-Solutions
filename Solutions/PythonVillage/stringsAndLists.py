#!/usr/bin/python

""" Link: http://rosalind.info/problems/ini3/"""

def getStringSlices(string, a, b, c, d):
    return string[a : b + 1] + ' ' + string[c : d + 1]

if __name__ == "__main__":
    a, b, c, d = 34, 43, 118, 125
    string = 'VczF3wq7jzYUAQYujltu9S4BzwMkAIK1cMSalvelinusevH5bz7F4Nofvx2IaoNFYpAzgaQZYkRUpW8pggL8yEzl2ZP6jv2MgA6S2w93Sdw5qjbFxNQsbHfasciatasR5NP4jsitBPo07a6U8ru7ArorRnmXXsSD.'
    substring = getStringSlices(string, a, b, c, d)
    print(substring)
