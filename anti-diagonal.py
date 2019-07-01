# Give a N*N square matrix, return an array of its anti-diagonals.


#arr = [[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]]

arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]


for row in arr:
    print(row)


def diagonal_printing():
    temp_arr = []
    k = 0

    while k < (len(arr)):
        k += 1
        for i in range(k):
            temp_arr.append(arr[k - 1 - i][i])

        print(temp_arr)
        temp_arr = []

    s = 0
    while s < len(arr)-1:
        s += 1
        for i in range(len(arr)-s):
            temp_arr.append(arr[len(arr) - i - 1][s+i])

        print(temp_arr)
        temp_arr = []


diagonal_printing()
