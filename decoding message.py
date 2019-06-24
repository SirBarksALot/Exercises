s = '12'
out = 0


def num_decode_ways(str_arr, output):
    if len(str_arr) != 0:
        if int(str_arr[0]) == 0:
            print('''Can't, sorry, 0 is first''')
        elif len(str_arr) == 1:
            return output + 1
        else:
            if int(str_arr[0]+str_arr[1]) <= 26:
                output += num_decode_ways(str_arr[2:], output)
            output += num_decode_ways(str_arr[1:], output)
    else:
        return output + 1

    return output


print(num_decode_ways(s, out))
