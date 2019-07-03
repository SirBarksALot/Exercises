import random

population = [i for i in range(10)]
tab = random.choices(population, weights=None, cum_weights=None, k=10)
print(tab)


def insertion_sort():
    for m in range(1, len(tab)):
        n = m - 1
        while tab[n+1] < tab[n]:
            tab[n], tab[n+1] = tab[n+1], tab[n]
            n -= 1
            if n < 0:
                break


insertion_sort()
print(tab)
