string = '1222311'


def occurence(input_string):
    arr = []
    arr_out = []
    for i in range(len(input_string)):
        arr.append(int(input_string[i]))
        if i+1 < len(input_string):
            if input_string[i] != input_string[i+1]:
                arr_out.append(arr)
                arr = []
        else:
            arr_out.append(arr)

    for j in range(len(arr_out)):
        arr_out[j] = (len(arr_out[j]), arr_out[j][0])

    return arr_out


print(occurence(string))
