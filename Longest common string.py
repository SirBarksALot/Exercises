# given two strings s1 and s2 find the longest common substring
s1 = 'salad'
s2 = 'lad'


def longest_common_substring():
    arr = []
    for x in range(len(s1)):
        for y in range(len(s2)):
            temp_arr = []
            i = 0
            j = 0
            while s1[x+i] == s2[y+j]:
                temp_arr.append(s1[x+i])
                i += 1
                j += 1
                if x+i >= len(s1) or y+j >= len(s2):
                    break

            if len(temp_arr) > 0:
                arr.append(temp_arr)

    longest_substring = []
    for element in arr:
        if len(element) > len(longest_substring):
            longest_substring = element

    return longest_substring


print(longest_common_substring())
