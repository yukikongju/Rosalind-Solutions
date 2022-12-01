#!/usr/bin/python

""" Link: http://rosalind.info/problems/fibd/"""

def getRabbitsRemaining(n, m):
    bunnies = [1, 1]
    months = 2
    while months < m:
        if months < m:
            bunnies.append(bunnies[-1] + bunnies[-2])
        elif months  == m:
            bunnies.append(bunnies[-1] + bunnies[-2] - 1)
        else:
            bunnies.append(bunnies[-1] + bunnies[-2] - 1 - bunnies[-(m + 1)])
    months += 1
    return bunnies[-1]
            
if __name__ == "__main__":
    n = 6
    m = 3
    rabbits = getRabbitsRemaining(n , m)
    print(rabbits)
