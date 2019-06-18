# You are given an array A of size N.
# The array contains integers and is of even length.
# The elements of the array represent N coin of values
# V1, V2, ....Vn.
# You play against an opponent in an alternating way.
# In each turn, a player selects either the first or last coin
# from the row, removes it from the row permanently,
# and receives the value of the coin.
# You need to determine the maximum possible amount of money
# you can win if you go first.

A = [8, 15, 3, 7]


def maximum_amount(arr, coin_sum):
    for i in range(2):
        # your move
        if i == 0:
            next_array = arr[1:]
            coin_sum += arr[0]
        else:
            next_array = arr[:-1]
            coin_sum += arr[-1]

        # opponent move
        if next_array[0] > next_array[-1]:
            next_array = next_array[1:]
        else:
            next_array = next_array[:-1]

        if len(next_array) > 1:
            maximum_amount(next_array, coin_sum)
        else:
            print(coin_sum)

        if i == 0:
            coin_sum -= arr[0]
        else:
            coin_sum -= arr[-1]


maximum_amount(A, 0)
