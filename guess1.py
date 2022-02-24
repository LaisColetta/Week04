#Program that prompts the user to guess a number until finds the correct one
#Author: Lais

a = (input('Please guess a number: '))

while a != 30:
    a = (input('Wrong\nPlease guess again: '))

print ('Well done! The number is {}' .format (a))