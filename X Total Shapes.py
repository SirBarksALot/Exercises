# Given N * M string array of O's and X's.
# The task is to find the number of 'X' total shapes.
# 'X' shape consists of one or more adjacent X's (diagonals not included).

N = 7
M = 4

arr = [['O', 'O', 'O', 'O', 'X', 'X', 'O'],
       ['O', 'X', 'O', 'X', 'O', 'O', 'X'],
       ['X', 'X', 'X', 'X', 'O', 'X', 'O'],
       ['O', 'X', 'X', 'X', 'O', 'O', 'O']]


def check():
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            print(arr[[]], end='')
        print('')


check()
