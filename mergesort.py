import random

population = [i for i in range(100)]
tab = random.choices(population, weights=None, cum_weights=None, k=8)
print(tab)


def dividing_list(num_list):
    if len(num_list) == 1:
        return num_list

    half_index = int(len(num_list)/2)
    tab_1 = num_list[:half_index]
    tab_2 = num_list[half_index:]
    print(tab_1)
    print(tab_2)

    return dividing_list(tab_1), dividing_list(tab_2)


dividing_list(tab)

