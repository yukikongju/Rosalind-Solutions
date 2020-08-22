#!/usr/bin/python

num = 6
string = '6 10 4 5 1 2'

def countSwapInInsertionSort(my_list, num):
    count = 0
    for i in range(1, len(my_list)):
        while (i > 0) and (my_list[i] < my_list[i - 1]):
            my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
            count += 1
            i -= 1
    return count

def convertStringToListOfNumbers(string):
    string_list = list(string.split(' '))
    return [int(num) for num in string_list]

def read_file(filename):
    f = open(filename, 'r')
    #  num = f.readlines()[0].strip()
    string = f.readlines()[1].strip()
    return string

if __name__ == "__main__":
    testname = '../../Files/insertion_sort_example.txt'
    filename = '../../Files/rosalind_ins.txt'
    string = read_file(filename)
    my_list = convertStringToListOfNumbers(string)
    #  print(my_list)
    num_swaps = countSwapInInsertionSort(my_list, num)
    print(num_swaps)


