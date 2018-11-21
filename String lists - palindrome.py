word = str(input('Word to check for palindrome:  '))

var1 = 'palindrom'

for i in range(0, len(word)//2):
    if word[i] == word[len(word)-1-i]:
        pass
    else:
        var1 = 'not palindrome'
        break
    
print(word + ' is ' + var1 + '!')
