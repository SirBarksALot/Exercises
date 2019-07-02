# Given two arrays A and B of equal size N,
# the task is to find if given arrays are equal or not.
# Two arrays are said to be equal if both of them contain same set of elements,
# arrangements (or permutation) of elements may be different though.
# Note : If there are repetitions, then counts of repeated elements must also
# be same for two array to be equal.

A = [1, 2, 5, 4, 0]
B = [2, 4, 5, 0, 1]


def check_if_the_same(arr1, arr2):
    for i in range(len(arr1)-1, -1, -1):
        for j in range(len(arr2)):
            print(arr1[i], arr2[j])
            if arr1[i] == arr2[j]:
                del arr1[i], arr2[j]
                break
    if len(arr1) == 0:
        return True
    else:
        return False


# print(check_if_the_same(A, B))


def check_if_the_same_hash(arr1, arr2):
    arr1_dict = {}
    for i in arr1:
        if f'{i}' in arr1_dict:
            arr1_dict[f'{i}'] += 1
        else:
            arr1_dict[f'{i}'] = 1

    for j in arr2:
        if f'{j}' in arr1_dict:
            arr1_dict[f'{j}'] -= 1
            if arr1_dict[f'{j}'] == 0:
                arr1_dict.pop(f'{j}')
        else:
            return False

    return True


print(check_if_the_same_hash(A, B))
