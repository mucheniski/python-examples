# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random

# listA = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# listB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89]

# Creating a random list
# This line of code will leave a containing a list of 10 random numbers from 0 to 99
listA = random.sample(range(100), 10)
listB = random.sample(range(100), 10)

print(f'List A {listA}')
print(f'List B {listB}')

listResutlt = [itemB for itemB in listB if itemB in listA]

print(f'List result {listResutlt}')