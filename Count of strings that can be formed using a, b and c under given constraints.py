# Given a length n,
# count the number of strings of length n that can be made
# using ‘a’, ‘b’ and ‘c’
# with at-most one ‘b’ and two ‘c’s allowed.

n = 3
letters_dict = {
    'a': -1,
    'b': 1,
    'c': 2
}
output = 0


def count_strings(n_len, letters):
    global output
    print(n_len, letters)
    if n_len > 0:
        for key, value in letters.items():
            print(key, value)
            if letters[key] != 0:
                count_strings(n_len - 1, letters)
                letters[key] -= 1
                if n_len == 1:
                    output += 1


count_strings(n, letters_dict)
print(output)
