# Given an input string and a dictionary of words,
# find out if the input string can be segmented into a space-separated sequence of dictionary words.

dictionary = {'i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice',
              'cream', 'icecream', 'man', 'go', 'mango'}

string = 'ilike'


def main(word):
    ok_list = []
    if word in dictionary:
        ok_list.append(word)
        print('{} found'.format(word))
    else:
        word.rstrip()
        print('{} not in dictionary'.format(word))


main(string)
