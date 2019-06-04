# Given an unsorted array A of size N of non-negative integers,
# find a continuous sub-array which adds to a given number S.

A = [2, 1, 3, 0, 5, 8, 9, 4, 5, 6, 7, 3, 2, 5, 1, 8]
N = len(A)
S = 10


def find_sub_array(array, s):
    index = 0

    for i in range(len(array)):
        print(s, index)
        s = s - array[i]
        print(s)
        if s == 0:
            return array[index:i+1]
        elif s > 0:
            index += 1
        else:
            index = i
            s = 10
        print(s, index)

    return 'No sublist matching given criteria!'


print(find_sub_array(A, S))
