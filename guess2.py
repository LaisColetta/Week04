#Program that tells if user guess is too high or low each time they guess.
#Author: Lais

a = 30
b = (input('Please guess a number: '))

while b != a:
    if b < a:
        print ('Too low')
        
    else:
        print(('Too high'))
        
    b = (input ("Please guess again: "))
    
print ('Well done! The number is {}' .format (a))
