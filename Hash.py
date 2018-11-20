import sys

hash_table = [None]*10
print(hash_table)


def hash_fct(wod):
    hashed_word = len(wod)

    return hashed_word % 10


def hashing_table(tab, word):
    hash_index = hash_fct(word)

    while tab[hash_index] is not None:
        if None in tab:
            if hash_index == 9:
                hash_index = 0
            else:
                hash_index += 1
        else:
            print('No more space!')
            sys.exit()

    tab[hash_index] = word

    return tab


while True:
    word_to_hash = str(input('Type word: '))
    print(hash_fct(word_to_hash))
    print(hashing_table(hash_table, word_to_hash))
