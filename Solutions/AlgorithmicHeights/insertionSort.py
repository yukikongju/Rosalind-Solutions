#!/usr/bin/python

num = 806
string = ''

def countSwapInInsertionSort(my_list, num):
    count = 0
    for i in range(2, len(my_list)):
        k = i
        while k > 1 and my_list[k] < my_list[k - 1]:
            count += 3  # swaping requires 3 actions
            k -= 1
    return count


def convertStringToListOfNumbers(string):
    string_list = list(string.split(' '))
    return [int(num) for num in string_list]


if __name__ == "__main__":
    my_list = convertStringToListOfNumbers(string)
    print(my_list)
    num_swaps = countSwapInInsertionSort(my_list, num)
    print(num_swaps)


