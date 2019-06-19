# Given a string S consisting only '0's and '1's,
# print the last index of the '1' present in it.


string = '010001'


def find_index(char):
    for i in range(len(string)-1, -1, -1):
        if string[i] == char:
            return i

    return 'Char not found'


print(find_index('1'))
