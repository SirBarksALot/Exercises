# Given an array arr[] of N non-negative integers representing height of
# blocks at index i as Ai where the width of each block is 1.
# Compute how much water can be trapped in between blocks after raining.
# Structure is like below:
# | |
# |_|
# We can trap 2 units of water in the middle gap.


arr = [1, 0]
water = 0
arr_cache = []


def trimm_zeros():
    first = 0
    last = 0
    for i in range(len(arr)):
        if last == 0:
            # trimm right zeros
            last = arr.pop()  # pop last item in a list
        if first == 0:
            # trimm left zeros
            first = arr[i]  # take first item in a list
            if first > 0:
                del arr[:i + 1]
        if last != 0 and first != 0:
            return last, first
    return 'No blocks > 0, or just one'


def trimm_right_zeros():
    for i in range(len(arr)):
        last = arr.pop()  # pop last item in a list
        if last > 0:
            return last
    return 'no blocks > 0'


def trimm_left_zeros(arr):
    for i in range(len(arr)):
        first = arr[i]  # take first item in a list
        if first > 0:
            del arr[:i+1]
            return first
    else:
        return 'no blocks > 0'

print(trimm_zeros())
print(arr)
# print(trimm_right_zeros())
# print(arr)
# print(trimm_left_zeros(arr))
# print(arr)
