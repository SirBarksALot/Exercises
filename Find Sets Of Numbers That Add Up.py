from itertools import combinations

lista = str(input('Your list of numbers: '))
num = int(input('Your choosen summ: '))

tab = []
suma = 0

for i in range(len(lista)):
    tab.append(list(combinations(lista, i)))


for tabs in tab:
    for i in range(len(tabs)):
        tabs[i] = [int(var) for var in tabs[i]]
        print(tabs[i], sum(tabs[i]))
        if sum(tabs[i]) == num:
            suma += 1
        else:
            pass

print(suma)
