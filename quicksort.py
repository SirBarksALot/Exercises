import random

population = [i for i in range(100)]
tab = random.choices(population, weights=None, cum_weights=None, k=10)
print(tab)


def quick_sort_function(tabl):
    pivot = tabl[-1]
    print("Pivot:", pivot)
    i = -1

    for j in range(len(tabl)-1):
        if tabl[j] < pivot:
            i += 1
            tabl[i], tabl[j] = tabl[j], tabl[i]

    quick_sort_function(tabl)

    return tabl


print(quick_sort_function(tab))
