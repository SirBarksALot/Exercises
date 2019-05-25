
def find_smallest(arr):
    buff = arr[0]
    for num in arr:
        if num < buff:
            buff = num
        else:
            pass
    return buff


def find_2nd_smallest(arr):
    min1 = arr[0]
    min2 = arr[0]

    for num in arr:
        if num < min1:
            min1, min2 = num, min1
        elif num < min2 and num > min1:
            min2 = num
        else:
            pass

        print(min1, min2)

    return min1, min2


tab = [8, 6, 6, 7, -15, 4, 3]
print(find_2nd_smallest(tab))
