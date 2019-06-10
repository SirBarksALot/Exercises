import random

population = [i for i in range(100)]
tab = random.choices(population, weights=None, cum_weights=None, k=10)
print(tab)

pivot_index = len(tab)//2
pivot = tab[pivot_index]
print('Pivot = {}'.format(pivot))


def quicksort_function(tab, pivot_index, i, var):
    if var == 'left':
        if tab[i] > tab[pivot_index]:
            tab[i], tab[pivot_index-1], tab[pivot_index] = tab[pivot_index-1], tab[pivot_index], tab[i]
        else:
            i += 1
    else:
        if tab[-i-1] < tab[pivot_index]:
            tab[-i-1], tab[pivot_index+1], tab[pivot_index] = tab[pivot_index+1], tab[pivot_index], tab[-i-1]
        else:
            i += 1

    print(tab)


quicksort_function(tab, pivot_index, 0, 'left')
quicksort_function(tab, pivot_index, 0, 'right')
