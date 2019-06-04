# Given an unsorted array A of size N of non-negative integers,
# find a continuous sub-array which adds to a given number S.

A = [1, 2, 7, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
S = 15


def find_sub_array(array, s):
    s_holder = s

    for j in range(len(array)):
        index = j
        for i in range(j, len(array)):
            s = s - array[i]
            if s == 0:
                return array[index:i+1]
            elif s < 0:
                s = s_holder
                break
            else:
                pass

            print(s, index)

    return 'No sublist matching given criteria!'


print(find_sub_array(A, S))
