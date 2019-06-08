import random

population = [i for i in range(100)]
tab = random.choices(population, weights=None, cum_weights=None, k=100)
print(tab)


def insertion_sort():
    for i in range(1, len(tab)):
        for j in range(i):
            if tab[i] < tab[j]:
                # swap
                tab[i], tab[j] = tab[j], tab[i]


insertion_sort()
print(tab)
