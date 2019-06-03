def string_reverse(string):
    x = list(string.strip())
    print(x)
    output = x[::-1]

    return output


input_word = 'ameba'
print(string_reverse(input_word))


def find_missing(tab1, tab2):
    tablo = set(tab1) - set(tab2)
    print(tablo)
    for elem in tab1:
        if elem not in tab2:
            return elem

    return None


print(find_missing(tab1=[4, 12, 9, 5, 6], tab2=[4, 9, 12, 6]))
