name = raw_input('What is your name?  ')
age = input('Age?  ')
loops = input('Amount of loops?  ')
age_till_100 = 100-age


print "Your name is: " + name
print "Your age is: ", age
print loops*("You are ", age_till_100, "years away from 100!")
