word = raw_input('Word to check for palindrome:  ')

var1 = 'palindrom'

for i in range(0, len(word)):
    if word[i] == word[len(word)-1-i]:
        pass
    else:
        var1 = 'not palindrom'
        break
    
print word + ' is ' + var1 + '!'
        
