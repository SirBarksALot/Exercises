def case_insensitive_comparison(str1, str2):
    if len(str1) != len(str2):
        return 'Different string size, not the same'

    for i in range(len(str1)):
        if ord(str1[i])-ord(str2[i]) != 0 and abs(ord(str1[i])-ord(str2[i])) != 32:
            return 'Not the same'

    return 'Same'


print(case_insensitive_comparison('adAm', 'adAM'))
