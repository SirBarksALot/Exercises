import random
import time

def roll():
    return random.randint(1,6)
    

while True:
    ask = raw_input('Roll a dice? [y/n]: ')
    if ask == 'y':
        num = input('How many times? ')
        t1 = time.clock()
        roll_mean = 0
        for i in range (0, num):
            roll_mean += roll()            
        t2 = time.clock()
        
        print ('Mean from all rolls: {}'.format(float(roll_mean)/float(num)))
        print ('Time for calculation: {}'.format(t2-t1))
        
    else:
        break
        
