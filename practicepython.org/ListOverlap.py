# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
from random import randint


def createList(list):
    for i in range(1, 6):
        list.append(randint(1, 100))


listA = list()
listB = list()

createList(listA)
createList(listB)

print(f'List A {listA}')
print(f'List B {listB}')


listCommon = []

for itenA in listA:
    for itenB in listB:
        if itenA == itenB:
            if itenB not in listCommon:
                listCommon.append(itenB)

print(f'Common numbers {listCommon}')
