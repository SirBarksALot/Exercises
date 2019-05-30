def finding_first_occurence(word):
    temp_table = []
    for letter in word:
        if letter in temp_table:
            return letter
        else:
            temp_table.append(letter)

    return 'Recurrence not found!'


word_to_search = str(input('Pick a word: '))
print(finding_first_occurence(word_to_search))
