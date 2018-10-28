lista = []
num = input('Choose number:   ')

for i in range (1,num+1):
    if num % i == 0:
        lista.append(i)
    else:
        pass

print num, ' is dividable by ', lista
        
