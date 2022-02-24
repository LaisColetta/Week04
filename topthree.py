#Program that generates 10 random numbers (0-100), prints them out then prints out the top three.
#Author: Lais

import random
randomlist = []
for i in range (0,10):
    n=random.randint(1,100)
    randomlist.append(n)
print ('10 random numbers: ' + str(randomlist))

list = randomlist
n = 3
list.sort(reverse=True)
print ('The top 3 are: ' + str(list[-n:]))




