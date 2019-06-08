import random

population = [i for i in range(100)]
tab = random.choices(population, weights=None, cum_weights=None, k=100)
print(tab)


def selection_sort():
    for j in range(len(tab)):
        current_max = tab[0]
        max_index = 0
        for i in range(len(tab)-j):
            if tab[i] > current_max:
                current_max = tab[i]
                max_index = i
        # swap max with the last
        tab[max_index], tab[-j-1] = tab[-j-1], tab[max_index]


selection_sort()
print(tab)
