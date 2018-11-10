import random

population = [i for i in range(100)]

tab = random.choices(population, weights=None, cum_weights=None, k=10)

print(tab)


def is_sorted(table):
    for i in range(len(table)-1):
        if table[i] <= table[i+1]:
            pass
        else:
            return False
    return True


def sorting(table):
    while not is_sorted(table):
        print(table)
        print(is_sorted(table))
        for i in range(len(table)-1):
            if table[i] > table[i+1]:
                table[i], table[i+1] = table[i+1], table[i]
            else:
                pass

    return table


print(sorting(tab))
print('Sorted')
