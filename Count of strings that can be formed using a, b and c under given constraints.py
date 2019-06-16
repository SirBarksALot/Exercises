# Given a length n,
# count the number of strings of length n that can be made
# using ‘a’, ‘b’ and ‘c’
# with at-most one ‘b’ and two ‘c’s allowed.

n = 4
letters_dict = {
    'a': -1,
    'b': 1,
    'c': 2
}


def count_strings(z, available_letters):
    output = 0
    z -= 1
    for key, value in available_letters.items():
        print(key, value)
        if value != 0:
            available_letters[key] -= 1
            if z > 0:
                output += count_strings(z, available_letters)
            elif z == 0:
                output += 1
            available_letters[key] += 1

    print(available_letters)
    print(output)
    return output


print(count_strings(n, letters_dict))
