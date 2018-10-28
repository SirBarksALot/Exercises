a = [1, 1, 2, 3, 5, 8, 11 ,13, 21, 34, 55, 89]
b = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21, 34]
new_list = []

if len(a) >= len(b):
    #a longer
    length = len(a)
    choosen_list = a
    search_list = b
else:
    #b longer
    length = len(b)
    choosen_list = b
    search_list = a

for i in range(0,length):
    if choosen_list[i] in search_list:
        new_list.append(choosen_list[i])
    else:
        pass

print new_list
        
