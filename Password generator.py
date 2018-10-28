import random

list_with_passwords = []

def generate_pass():
    password = []
    chars_amount = random.randrange(6,11,1)
    
    for i in range (0, chars_amount):
        character = random.randrange(33,126,1)
        password.append(str(unichr(character)))
    print ''.join(password)
    
    list_with_passwords.append(''.join(password))

var_for_while_loop = 1

while var_for_while_loop != 0:
    var1 = raw_input('Generate new password? [y/n]: ')
    if var1 == 'y':
        generate_pass()
    else:
        var_for_while_loop = 0

    print list_with_passwords
