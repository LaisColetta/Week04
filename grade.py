#Program that reads in a students percentage mark and prints out corresponding the grade.
#Author: Lais

a = float(input('Enter percentage: '))
if (a >= 70):
    print('Distinction')
elif (a >= 60):
    print ('Merit 1')
elif (a>=50):
    print ('Merit 2')
elif (a>=40):
    print ('Pass')
elif (a<40):
    print('Fail')
