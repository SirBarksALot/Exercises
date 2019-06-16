# Given an array A of N integers.
# The task is to find a peak element in it.
# An array element is peak
# if it is not smaller than its neighbours.
# For corner elements, we need to consider only one neighbour.
# Note: There may be multiple peak element possible,
# in that case you may return any valid index.

A = [3, 4]


def find_peak():
    for i in range(len(A)):
        if i == 0:
            if A[i] >= A[i+1]:
                return i, A[i]
        elif i == len(A)-1:
            if A[i] >= A[i-1]:
                return i, A[i]
        elif A[i] >= A[i-1] and A[i] >= A[i+1]:
            return i, A[i]


print(find_peak())
