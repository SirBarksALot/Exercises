def string_reverse1(string):
    x = list(string.strip())
    output = x[::-1]
    output = ''.join(output)

    return output


input_word = 'amebas'
print(string_reverse1(input_word))


def string_reverse2(string):
    output = ''
    for x in string:
        output = x + output

    return output


print(string_reverse2(input_word))


def string_reverse3(string):
    output = list(string)
    x = int((len(string)/2))
    for i in range(x):
        output[i], output[-i-1] = output[-i-1], output[i]

    output = ''.join(output)

    return output


print(string_reverse3(input_word))
