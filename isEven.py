#Program tha asks the user to enter in a number, and the program will tell the user if the number is even or odd
#Author: Lais

a = int(input('Enter a number: '))
if a%2 == 0:
    print ('{} is even'.format(a))
else:
    print ("{} is odd".format(a))
