list = [10.0, 8, 7.5, 4.9, 9.0, 1.3]

print(len(list))
print(sum(list))

# Sorted produce a new sorted list
print(sorted(list))

# the method sort don't create a new list, only change de original list
list.sort()
print(list)

#  custom function
def add1(a):
    """

    :param a:
    :return: add 1 to a
    """
    b = a + 1
    return b

print(add1(10))


def printName():
    print("Diego")

printName()


album_ratings = [10.0, 8.5, 9.5]

def printStuff(stuff):
    for i,s in enumerate(stuff):
        print("Algum ", i , "Rating is ", s)

printStuff(album_ratings)


#  To recaive more tha one element put a *
def artistNames(*names):
    for name in names:
        print(name)

artistNames("Diego", "Bruna", "loki")


#  if the variable don't exist in local scope, python search in global scope
def ACDC(y):
    print(Rating)
    return (Rating+y)

Rating = 9
z =  ACDC(1)

print(Rating)

#  if you put global in a function scope variable, than the variable will be global
def pinkFloyd():
    global ClaimedSales
    ClaimedSales = "45 milion"
    return ClaimedSales

pinkFloyd()
print(ClaimedSales)

