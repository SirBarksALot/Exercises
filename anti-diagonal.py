# Give a N*N square matrix, return an array of its anti-diagonals.


arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

for row in arr:
    print(row)


def diagonal_printing():
    temp_arr = []
    k = 0

    while k < (len(arr)):
        k += 1
        for i in range(k):
            temp_arr.append(arr[i][k - 1 - i])

        print(temp_arr)
        temp_arr = []

    k = 0
    while k < (len(arr))-1:
        k += 1
        print(k)
        for i in range(k, len(arr)):
            temp_arr.append(arr[i][len(arr) - i])

        print(temp_arr)
        temp_arr = []


diagonal_printing()
