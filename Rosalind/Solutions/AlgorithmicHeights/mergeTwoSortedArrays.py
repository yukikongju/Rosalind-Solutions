#!/usr/bin/python

""" Keep track of indexes for each array, and compare element to add it in
third array."""
def merge_sort(A, B):
    i, j = 0, 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else: # A[i] > B[j]
            C.append(B[j])
            j += 1
    # Add the rest of the elements. Only one of the array will be empty
    C += A[i:] + B[j:]
    return C

def read_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    arr1 = [int(i) for i in lines[1].strip().split(' ')]
    arr2 = [int(i) for i in lines[3].strip().split(' ')]
    return arr1, arr2

def print_list(sorted_array):
    for element in sorted_array:
        print(element, end = ' ')

if __name__ == "__main__":
    #  filename = '../../Files/merge_two_sorted_arrays.txt'
    filename = '../../Files/rosalind_mer.txt'
    arr1, arr2 = read_file(filename)
    #  print(arr1, arr2)
    sorted_array = merge_sort(arr1, arr2)
    print_list(sorted_array)
