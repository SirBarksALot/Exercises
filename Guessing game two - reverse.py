import random
import sys

beg = input('Type starting number:  ')
fin = input('Type ending number:  ')
var1 = 1
guess_amount = 0

print beg, fin

def guess(start, end):
    guess_num = (start + end) // 2
    return guess_num

while True:
    guess_amount += 1
    print guess(beg, fin)
    input_var1 = raw_input('Is it this number?[y/n]  ')
    if input_var1 == 'y':
        print 'Yay PC is smart!'
        print 'Number of guesses needed:  ', guess_amount
        sys.exit()
    else:
        input_var2 = raw_input('Too high or too low?[2high/2low]  ')
        if input_var2 == '2high':
            fin = guess(beg, fin)
        else:
            beg = guess(beg, fin)
