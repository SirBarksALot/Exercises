arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr_len = 10


def find_missing():
    for i in range(0, arr_len):
        if i == (arr_len-1) or i + 1 != arr[i]:
            return i+1


print(find_missing())
