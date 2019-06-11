# Given an array arr[] of N non-negative integers representing height of
# blocks at index i as Ai where the width of each block is 1.
# Compute how much water can be trapped in between blocks after raining.
# Structure is like below:
# | |
# |_|
# We can trap 2 units of water in the middle gap.


arr = [2, 0, 2, 0]


def trimm_right_zeros():
    for i in range(len(arr)):
        last = arr.pop()  # pop last item in a list
        if last > 0:
            return last
    print('no blocks > 0')
    return False


def trimm_left_zeros(arr):
    for i in range(len(arr)):
        first = arr[i]  # take first item in a list
        if first > 0:
            del arr[:i+1]
            return first

    return False


def trimm_zeros(arr):
    last = trimm_right_zeros()
    if last is not False:
        first = trimm_left_zeros(arr)
        if first is not False:
            return first, last

    return False


def count_water():
    outside_set = trimm_zeros(arr)
    if outside_set is False:
        return 'No blocks, or just 1'
    else:
        if outside_set[1] > outside_set[0]:
            higher = outside_set[0]
        else:
            higher = outside_set[1]

    water = higher * len(arr)

    return water


print(count_water())
