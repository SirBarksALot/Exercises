import random
import sys

gen_num = str(random.randrange(1000,9999,1))
guess_num = 0
print gen_num

def add_cow(cow):
    cow += 1
    return cow

def add_bull(bull):
    bull += 1
    return bull

def checking(gen_num, guess):
    cow = 0
    bull = 0
    for i in range(0, len(gen_num)):
        if gen_num[i] == guess[i]:
            cow += 1
        elif guess[i] in gen_num:
            bull += 1
        else:
            pass
        
    if cow == 4:
        print 'You are right, it took you only:', guess_num, 'time(s).'
        output = 1
    else:
        print cow,'-cows',bull,'-bulls'
        output = 0
        
    return output

while True:
    guess = raw_input('Try to guess 4-digit number:  ')
    guess_num += 1
    
    if  checking(gen_num, guess) == 1:
        sys.exit()
    else:
        pass


