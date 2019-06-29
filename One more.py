arr = [9, 9, 9, 9]


def add_one(arry, i):
    arry[-i] += 1
    if arry[-i] == 10:
        arry[-i] = 0
        if i != len(arry):
            add_one(arry, i+1)
        else:
            # arry.insert(0, 1)
            arry.append(0)
            arry[0] = 1
    print(arry)


def add_one_iter():
    for i in range(len(arr)):
        arr[-i - 1] += 1
        if arr[-i - 1] < 9:
            break
        else:
            arr[-i - 1] = 0
            if abs(-i - 1) == len(arr):
                # arr.insert(0, 1)
                arr.append(0)
                arr[0] = 1
                break

    print(arr)


add_one(arr, 1)
add_one_iter()
