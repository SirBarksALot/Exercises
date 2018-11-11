import random

population = [i for i in range(100)]

tab = random.choices(population, weights=None, cum_weights=None, k=10)

print(tab)


def sorting(table):
    while True:
        print(table)
        check_var = 0
        for i in range(len(table)-1):
            if table[i] > table[i+1]:
                check_var = 1
                table[i], table[i+1] = table[i+1], table[i]
            else:
                pass

        if check_var == 0:
            break
        else:
            pass

    return 'Sorted table:\n{}'.format(table)


print(sorting(tab))
