# Given an array A[] of N elements.
# The task is to complete the function which returns true
# if triplets (following) exists in array A whose sum is zero
# else returns false.

A = [0, -1, 2, -3, 1]


def find_triples():
    if len(A) < 3:
        return False

    for i in range(1, len(A)-1):
        a = A[i-1]
        b = A[i]
        c = A[i+1]
        if a+b+c == 0:
            return True

    return False


print(find_triples())
