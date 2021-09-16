# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?


number = int(input('Put one number please: '))
checkNumber = int(input('Put another number to divide the first please: '))

if number % 2 == 0:

    # If the number is a multiple of 4, print out a different message.
    if number % 4 == 0:
        print('Even and multiple of four')
    else:
        print('Even')
else:
    print('Odd')

print('='*300)

# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
if number % checkNumber == 0:
    print('Tha nambers are divided correctly')
else:
    print('The numbers are not divideble')