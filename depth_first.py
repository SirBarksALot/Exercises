arr = [['b', 'b', 'w', 'b'],
       ['r', 'r', 'w', 'r'],
       ['b', 'w', 'w', 'b']]


def check_adjacent(y, x, arr, visited):
    color = arr[y][x]
    visited[f'[{y}][{x}]'] = True

    if x + 1 < len(arr[y]):
        if arr[y][x + 1] == color and f'[{y}][{x+1}]' not in visited:
            check_adjacent(y, x + 1, arr, visited)

    if x - 1 >= 0:
        if arr[y][x - 1] == color and f'[{y}][{x-1}]' not in visited:
            check_adjacent(y, x - 1, arr, visited)

    if y - 1 >= 0:
        if arr[y - 1][x] == color and f'[{y-1}][{x}]' not in visited:
            check_adjacent(y - 1, x, arr, visited)

    if y + 1 < len(arr):
        if arr[y + 1][x] == color and f'[{y+1}][{x}]' not in visited:
            check_adjacent(y + 1, x, arr, visited)

    return visited


# print(check_adjacent(1, 1, arr, visited={}))

def find_largest_pool(arr):
    output = 0
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            var = len(check_adjacent(j, i, arr, visited={}))
            if var > output:
                output = var

    return output


print(find_largest_pool(arr))
