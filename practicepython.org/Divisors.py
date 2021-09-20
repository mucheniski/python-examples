# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

inputNumber = int(input('Put one number please '))
divisorsList = []

for n in range(1, inputNumber + 1):
    if inputNumber % n == 0:
        divisorsList.append(n)

print(divisorsList)