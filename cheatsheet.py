# Given an array A of size N.
# The elements of the array consists of positive integers.
# You have to find the largest element with minimum frequency.


def find_max():
    maxi = 0
    for i in A:
        if i > maxi:
            maxi = i

    return maxi


A = [423, 42, 4234235, 564, 74675, 345242, 235, 534535, 52423, 123]
N = len(A)
print(find_max())
