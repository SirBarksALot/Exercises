# find 3rd biggest numberin a set s


s = (5, 43, 5643, 543, 312, 543, 16, 4365, 43)
set_var = set(s)

print(set_var)


def third_max():
    arr = [0]*3
    for x in set_var:
        if x > arr[0]:
            arr[0] = x
        elif x > arr[1]:
            arr[1] = x
        elif x > arr[2]:
            arr[2] = x
        else:
            pass

    return arr[2]


print(third_max())
