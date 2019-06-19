arr = [1, 2, 3, 4, 5, 6, 7, 8, 10]
arr_len = 10


def find_missing():
    for i in range(0, arr_len-1):
        if i + 1 != arr[i]:
            return i+1
    return arr_len


print(find_missing())
