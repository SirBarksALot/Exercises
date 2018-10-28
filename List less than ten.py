lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 4]
lista_2 = []
num = input("Number to check:  ")

for i in range (0,len(lista)):
    if lista[i] < num:
        lista_2.append(lista[i])
    else:
        pass

print lista_2
