import random

population = [i for i in range(1000)]
tab = random.choices(population, weights=None, cum_weights=None, k=500)
print(tab)


def merge_sort(tab):
    print(tab)
    if len(tab) > 1:
        first_half = tab[:(len(tab)//2)]
        second_half = tab[(len(tab)//2):]

        merge_sort(first_half)
        merge_sort(second_half)

        x = 0
        y = 0
        z = 0

        while x < len(first_half) and y < len(second_half):
            if first_half[x] < second_half[y]:
                tab[z] = first_half[x]
                x += 1
            else:
                tab[z] = second_half[y]
                y += 1

            z += 1

        while x < len(first_half):
            tab[z] = first_half[x]
            x += 1
            z += 1

        while y < len(second_half):
            tab[z] = second_half[y]
            y += 1
            z += 1


merge_sort(tab)
print(tab)
