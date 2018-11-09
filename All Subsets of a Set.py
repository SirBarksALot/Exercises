import itertools

word = str(input('Type a string: '))

print(word)

answer = []

for i in range(len(word)+1):
    answer.append(list(itertools.combinations(word, i)))

print(answer)
