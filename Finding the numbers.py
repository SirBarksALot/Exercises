# You are given an array A containing 2*N+2 positive numbers,
# out of which 2*N numbers exist in pairs
# whereas the other two number occur exactly once
# and are distinct. You need to find the other two numbers.

A = [1, 2, 3, 2, 1, 4]


def find_miss_paired():
    temp_dict = {}
    for num in A:
        if num not in temp_dict:
            temp_dict[num] = 1
        else:
            del temp_dict[num]

    return temp_dict


print(find_miss_paired())
