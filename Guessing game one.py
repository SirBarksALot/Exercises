import random

continue_var = 1
var_1 = 0

while continue_var != 0:
    
    szukana = random.randrange(1,10,1)
    print szukana

    while continue_var != 0:
        user_guess = raw_input('Your guess?: ')
        
        if user_guess == 'exit':
            continue_var = 0
            break
        elif int(user_guess) > szukana:
            print 'Try lower!'
            var_1 += 1
        elif int(user_guess) < szukana:
            print 'Try higher!'
            var_1 += 1
        elif int(user_guess) == szukana:
            print 'You are right!'
            var_1 += 1
            continue_var = 0
        else:
            print 'Sth went wrong!'
    print 'Number of tries: ', var_1
