word = str(input('Pick a word: '))
global i


def finding_recurence(word):
    for i in range(len(word)):
        for ii in range(i+1, len(word)):
            if word[i] == word[ii]:
                return 'First letter recurrence: {}'.format(word[i])
            else:
                pass
    return 'Recurrence not found!'


print(finding_recurence(word))
