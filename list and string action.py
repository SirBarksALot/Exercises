# given list s = ['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ',
# 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't']
# transform it into 'perfect' 'makes' 'practice'


s = ['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't']


def full_str_extract():
    output_arr = []
    arr = []
    for i in range(len(s)):
        if s[i] != ' ':
            arr.append(s[i])
        else:
            output_arr.append(arr)
            arr = []

    output_arr.append(arr)

    for j in range(len(output_arr)):
        output_arr[j] = ''.join(output_arr[j])

    output_arr.reverse()

    return output_arr


print(full_str_extract())
