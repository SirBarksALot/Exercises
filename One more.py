arr = [9, 9, 8, 9]


def add_one(arry, i):
    arry[-i] += 1
    if arry[-i] == 10:
        arry[-i] = 0
        if i != len(arry):
            add_one(arry, i+1)
        else:
            arry.insert(0, 1)
    print(arry)


add_one(arr, 1)
