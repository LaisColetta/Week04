#Program that keeps reading numbers until the user enters a 0.
#Author: Lais

list = []

num1 = int(input('Enter a number (0 to quit): '))

while num1 !=0:
    list.append(num1)

    num1 = int(input('Enter another number (0 to quit): '))

    for value in list:
        print (value)

    average = float (sum(list)) / len(list)
    print ('The average is {}'.format (average))
